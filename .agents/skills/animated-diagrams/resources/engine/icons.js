/* Registro de iconos para las specs de flujo: así las specs son datos puros (un nombre de
   icono) y no arrastran imports de React. */
import {
  Activity,
  AlertTriangle,
  Bell,
  Bot,
  Cable,
  CheckCircle2,
  CircuitBoard,
  Cpu,
  Database,
  Factory,
  Gauge,
  HardDrive,
  LayoutDashboard,
  Lock,
  Radio,
  RefreshCw,
  Server,
  ShieldCheck,
  Smartphone,
  Timer,
  Usb,
  Wifi,
  WifiOff,
  Zap
} from 'lucide-react';

export const FLOW_ICONS = {
  Activity,
  AlertTriangle,
  Bell,
  Bot,
  Cable,
  CheckCircle2,
  CircuitBoard,
  Cpu,
  Database,
  Factory,
  Gauge,
  HardDrive,
  LayoutDashboard,
  Lock,
  Radio,
  RefreshCw,
  Server,
  ShieldCheck,
  Smartphone,
  Timer,
  Usb,
  Wifi,
  WifiOff,
  Zap
};

export const getFlowIcon = (name) => FLOW_ICONS[name] || Activity;
