import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_docx(docx_path):
    try:
        doc = zipfile.ZipFile(docx_path)
        content = doc.read('word/document.xml')
        tree = ET.XML(content)
        
        word_namespace = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        
        paragraphs = []
        for p in tree.iter(f'{word_namespace}p'):
            texts = [node.text for node in p.iter(f'{word_namespace}t') if node.text]
            if texts:
                paragraphs.append(''.join(texts))
        return '\n'.join(paragraphs)
    except Exception as e:
        return str(e)

print("OBSERVACIONES:")
print(extract_text_from_docx(sys.argv[1]))
print("\n" + "="*50 + "\n")
print("SOLUCIONES:")
print(extract_text_from_docx(sys.argv[2]))
