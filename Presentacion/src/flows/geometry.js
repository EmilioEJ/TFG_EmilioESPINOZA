/* Geometría de las aristas de los diagramas de flujo.
   Las specs declaran los nodos en porcentaje del lienzo; aquí se traduce todo a unidades
   del viewBox del SVG para que las líneas salgan y entren exactamente del borde de cada caja. */

const sub = (a, b) => ({ x: a.x - b.x, y: a.y - b.y });
const add = (a, b) => ({ x: a.x + b.x, y: a.y + b.y });
const mul = (a, k) => ({ x: a.x * k, y: a.y * k });
const len = (a) => Math.hypot(a.x, a.y);

const norm = (a) => {
  const l = len(a);
  return l === 0 ? { x: 0, y: 0 } : { x: a.x / l, y: a.y / l };
};

/* Rectángulo del nodo en unidades del viewBox. La spec da x/y como centro y w/h como
   tamaño, ambos en % del lienzo. */
export function nodeRect(node, viewBox) {
  return {
    cx: (node.x / 100) * viewBox.w,
    cy: (node.y / 100) * viewBox.h,
    hw: (node.w / 100) * viewBox.w / 2,
    hh: (node.h / 100) * viewBox.h / 2
  };
}

/* Punto donde el rayo centro→objetivo corta el borde del nodo, separado por `gap`. */
function anchor(rect, toward, gap) {
  const dx = toward.x - rect.cx;
  const dy = toward.y - rect.cy;
  if (dx === 0 && dy === 0) return { x: rect.cx, y: rect.cy };

  const sx = dx !== 0 ? (rect.hw + gap) / Math.abs(dx) : Infinity;
  const sy = dy !== 0 ? (rect.hh + gap) / Math.abs(dy) : Infinity;
  const s = Math.min(sx, sy);

  return { x: rect.cx + dx * s, y: rect.cy + dy * s };
}

/* Polilínea suavizada: recorta cada vértice interior y lo sustituye por una curva
   cuadrática, para que los quiebres no se vean en ángulo recto duro. */
function roundedPath(pts, radius) {
  if (pts.length < 2) return '';

  const f = (n) => Number(n.toFixed(1));
  let d = `M ${f(pts[0].x)} ${f(pts[0].y)}`;

  for (let i = 1; i < pts.length - 1; i++) {
    const p = pts[i];
    const inDir = norm(sub(pts[i - 1], p));
    const outDir = norm(sub(pts[i + 1], p));
    const rIn = Math.min(radius, len(sub(pts[i - 1], p)) / 2);
    const rOut = Math.min(radius, len(sub(pts[i + 1], p)) / 2);
    const a = add(p, mul(inDir, rIn));
    const b = add(p, mul(outDir, rOut));
    d += ` L ${f(a.x)} ${f(a.y)} Q ${f(p.x)} ${f(p.y)} ${f(b.x)} ${f(b.y)}`;
  }

  const last = pts[pts.length - 1];
  return `${d} L ${f(last.x)} ${f(last.y)}`;
}

/* Punto situado a la fracción `t` del recorrido total de la polilínea. Se usa para colgar
   la etiqueta de la arista sin depender de getTotalLength() del DOM. */
function pointAt(pts, t) {
  const segments = [];
  let total = 0;

  for (let i = 1; i < pts.length; i++) {
    const l = len(sub(pts[i], pts[i - 1]));
    segments.push(l);
    total += l;
  }
  if (total === 0) return pts[0];

  let target = total * t;
  for (let i = 0; i < segments.length; i++) {
    if (target <= segments[i]) {
      const k = segments[i] === 0 ? 0 : target / segments[i];
      return add(pts[i], mul(sub(pts[i + 1], pts[i]), k));
    }
    target -= segments[i];
  }
  return pts[pts.length - 1];
}

/* Traza una arista entre dos nodos. `via` son waypoints opcionales en % del lienzo, para
   sacar la línea de encima de otras cajas. */
export function buildEdge(edge, nodesById, viewBox, { gap = 7, radius = 16 } = {}) {
  const from = nodesById[edge.from];
  const to = nodesById[edge.to];
  if (!from || !to) {
    console.warn(`[flows] arista "${edge.id}" apunta a un nodo inexistente`);
    return null;
  }

  const rFrom = nodeRect(from, viewBox);
  const rTo = nodeRect(to, viewBox);
  const waypoints = (edge.via || []).map((p) => ({
    x: (p.x / 100) * viewBox.w,
    y: (p.y / 100) * viewBox.h
  }));

  const firstTarget = waypoints[0] || { x: rTo.cx, y: rTo.cy };
  const lastTarget = waypoints[waypoints.length - 1] || { x: rFrom.cx, y: rFrom.cy };

  const start = anchor(rFrom, firstTarget, gap);
  const end = anchor(rTo, lastTarget, gap);
  const pts = [start, ...waypoints, end];

  /* Punto medio geométrico del recorrido. Es donde va el aspa de "enlace cortado": sobre la
     línea misma, no donde acabe cayendo el rótulo. */
  const medio = pointAt(pts, 0.5);

  return {
    ...edge,
    d: roundedPath(pts, radius),
    pts,
    label: edge.label,
    midX: medio.x,
    midY: medio.y
  };
}

/* ─────────────────────────────────────────────────────────────────────────────
   Colocación automática de los rótulos de arista.

   Antes cada rótulo se apartaba a mano con labelDx/labelDy. Eso se ajustaba mirando
   UNA etapa, y en las demás el mismo rótulo acababa encima de una caja, encima del
   título de una zona o tan lejos de su flecha que ya no se sabía a cuál pertenecía.

   Aquí se elige la posición por búsqueda: se prueban puntos a lo largo del recorrido y
   separaciones perpendiculares a él, y se puntúa cada candidato. Gana el de menor coste.
   Como sólo se rotulan las aristas de la etapa activa, el conjunto a resolver es pequeño
   (2–4 rótulos) y la búsqueda es inmediata.
   ──────────────────────────────────────────────────────────────────────────── */

/* Avance medio de JetBrains Mono 700 a 13u, medido sobre el render real. El alto incluye
   el aire del chip que va detrás del texto. */
const CHAR_W = 7.55;
const LABEL_H = 20;
const LABEL_PAD_X = 7;

export function labelBox(text, x, y) {
  const w = text.length * CHAR_W + LABEL_PAD_X * 2;
  return { x: x - w / 2, y: y - LABEL_H / 2, w, h: LABEL_H, x2: x + w / 2, y2: y + LABEL_H / 2 };
}

const overlap = (a, b) => {
  const ix = Math.min(a.x2, b.x2) - Math.max(a.x, b.x);
  const iy = Math.min(a.y2, b.y2) - Math.max(a.y, b.y);
  return ix > 0 && iy > 0 ? ix * iy : 0;
};

const rectOf = (node, viewBox) => {
  const r = nodeRect(node, viewBox);
  return { x: r.cx - r.hw, y: r.cy - r.hh, x2: r.cx + r.hw, y2: r.cy + r.hh };
};

/* Caja aproximada del título de una zona: se pinta en (x+14, y+22) con 13u y mayúsculas. */
const zoneLabelRect = (z, viewBox) => {
  const x = (z.x / 100) * viewBox.w + 14;
  const y = (z.y / 100) * viewBox.h + 22;
  return { x: x - 4, y: y - 15, x2: x + z.label.length * 8.4 + 4, y2: y + 6 };
};

/* Punto y dirección de la polilínea a la fracción t. */
function frameAt(pts, t) {
  const segs = [];
  let total = 0;
  for (let i = 1; i < pts.length; i++) {
    const l = len(sub(pts[i], pts[i - 1]));
    segs.push(l);
    total += l;
  }
  if (total === 0) return { p: pts[0], dir: { x: 1, y: 0 } };

  let target = total * Math.min(Math.max(t, 0), 1);
  for (let i = 0; i < segs.length; i++) {
    if (target <= segs[i] || i === segs.length - 1) {
      const k = segs[i] === 0 ? 0 : Math.min(target / segs[i], 1);
      return {
        p: add(pts[i], mul(sub(pts[i + 1], pts[i]), k)),
        dir: norm(sub(pts[i + 1], pts[i]))
      };
    }
    target -= segs[i];
  }
  return { p: pts[pts.length - 1], dir: { x: 1, y: 0 } };
}

/* Un rótulo posado en MITAD de su flecha es correcto: el chip la interrumpe y así no hay
   duda de a qué arista pertenece. Lo que no puede tapar son los extremos, porque ahí están
   la punta y el arranque, que es lo que dice de dónde viene y adónde va. */
function tapaExtremos(pts, box) {
  const dentro = (t) => {
    const { p } = frameAt(pts, t);
    return p.x > box.x && p.x < box.x2 && p.y > box.y && p.y < box.y2;
  };
  let n = 0;
  for (let k = 0; k <= 6; k++) {
    if (dentro((k / 6) * 0.18)) n++;              // arranque
    if (dentro(0.82 + (k / 6) * 0.18)) n++;       // punta de flecha
  }
  return n;
}

const T_CANDIDATOS = [0.5, 0.44, 0.56, 0.38, 0.62, 0.3, 0.7, 0.22, 0.78];

/* Niveles de separación respecto a la línea, no distancias fijas. El nivel 0 posa el chip
   sobre la arista; a partir del 1 se aparta lo justo para que su BORDE quede libre, que es
   lo que depende de la orientación: junto a una flecha vertical hay que apartar medio ancho
   del chip, y junto a una horizontal medio alto. Con distancias fijas, un rótulo largo
   seguía cruzando la línea por muy lejos que se pusiera su centro. */
const NIVELES = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5];

/* Radio del rectángulo en la dirección (nx, ny). */
const radioEnDireccion = (w, h, nx, ny) => (Math.abs(nx) * w + Math.abs(ny) * h) / 2;

/**
 * Coloca los rótulos de las aristas activas evitando cajas, títulos de zona y otros
 * rótulos. Devuelve un mapa id → { x, y, box }.
 *
 * @param activos aristas ya construidas (con .pts) que llevan rótulo en esta etapa
 */
export function layoutLabels(activos, { nodes, zones = [], viewBox }) {
  /* Muestreo de cada trazo activo, para poder comprobar que un rótulo no se posa sobre la
     línea de OTRA arista: si lo hace, el lector no sabe a cuál de las dos rotula. */
  const muestras = new Map(
    activos.map((e) => {
      const pts = [];
      for (let k = 0; k <= 60; k++) pts.push(frameAt(e.pts, k / 60).p);
      return [e.id, pts];
    })
  );

  const cajas = nodes.map((n) => rectOf(n, viewBox));
  const titulos = zones.map((z) => zoneLabelRect(z, viewBox));
  const colocados = [];
  const salida = {};

  /* Los rótulos largos se resuelven primero: son los que menos sitio tienen. */
  const orden = [...activos].sort((a, b) => (b.label || '').length - (a.label || '').length);

  for (const e of orden) {
    if (!e.label) continue;
    let mejor = null;

    for (const t of T_CANDIDATOS) {
      const { p, dir } = frameAt(e.pts, t);
      const nx = -dir.y;
      const ny = dir.x;

      const media = labelBox(e.label, 0, 0);
      const radio = radioEnDireccion(media.w, media.h, nx, ny);

      for (const nivel of NIVELES) {
        const off = nivel === 0 ? 0 : Math.sign(nivel) * (radio + 9 + (Math.abs(nivel) - 1) * 17);
        const x = p.x + nx * off;
        const y = p.y + ny * off;
        const box = labelBox(e.label, x, y);

        let coste = 0;
        /* Fuera del lienzo: inaceptable. */
        if (box.x < 2 || box.y < 2 || box.x2 > viewBox.w - 2 || box.y2 > viewBox.h - 2) coste += 1e6;
        /* Encima de una caja o del título de una zona: lo que producía el "texto sobre texto". */
        /* Un rótulo encima de una caja es el defecto más visible de todos: se penaliza muy
           por encima de lo que cuesta separarse de la línea. */
        for (const c of cajas) coste += overlap(box, c) * 60;
        for (const z of titulos) coste += overlap(box, z) * 30;
        /* Encima de otro rótulo de la misma etapa. */
        for (const c of colocados) coste += overlap(box, c) * 40;
        /* Encima de la línea de otra arista: el rótulo pasaría a leerse como suyo. Pesa más
           que apartarse del todo, porque un rótulo lejano se resuelve con un tirante y uno
           ambiguo no se resuelve de ninguna manera. */
        for (const [id, pts2] of muestras) {
          if (id === e.id) continue;
          for (const q of pts2)
            if (q.x > box.x && q.x < box.x2 && q.y > box.y && q.y < box.y2) coste += 700;
        }
        /* Tapando la punta o el arranque de su propia flecha. */
        coste += tapaExtremos(e.pts, box) * 900;
        /* Preferencias suaves: pegado a la línea antes que lejos de ella, y cerca del punto
           pedido. Separarse penaliza más que deslizarse a lo largo del trayecto, porque un
           rótulo alejado deja de leerse como parte de esa flecha. */
        coste += Math.abs(off) * 9;
        coste += Math.abs(t - (e.labelAt ?? 0.5)) * 180;

        if (!mejor || coste < mejor.coste) mejor = { x, y, box, coste, ancla: p };
      }
    }

    if (mejor) {
      colocados.push(mejor.box);
      /* Separación entre el chip y el punto del que cuelga. Si el rótulo tuvo que apartarse
         mucho (porque no cabía al lado de su flecha), se dibujará un tirante hasta el ancla
         para que no quede ninguna duda de a qué arista pertenece. */
      const dx = Math.max(mejor.box.x - mejor.ancla.x, 0, mejor.ancla.x - mejor.box.x2);
      const dy = Math.max(mejor.box.y - mejor.ancla.y, 0, mejor.ancla.y - mejor.box.y2);
      salida[e.id] = {
        x: mejor.x,
        y: mejor.y,
        box: mejor.box,
        ancla: mejor.ancla,
        tirante: Math.hypot(dx, dy) > 16
      };
    }
  }

  return salida;
}
