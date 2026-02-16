# 👨‍🦱 Hugo Bot — Asistente 3D para convertir Word a XML Moodle

Hugo Bot es una herramienta creada para profesores y centros educativos que necesitan transformar exámenes tipo test en formato Word (.docx) en **XML compatible con Moodle**, sin errores y sin necesidad de editar nada manualmente.

El sistema detecta automáticamente:

- Preguntas numeradas (1., 1), 1-, 1º…)
- Opciones tipo test (a), b., c), d)…)
- La respuesta correcta aunque esté marcada de cualquier forma:
  - **Negrita**
  - _Subrayado_
  - Color
  - Resaltado
  - Marcas como X, *, ✔
- Preguntas dentro de **tablas**
- Formatos desordenados o inconsistentes

Además, incluye:

- Un **avatar 3D interactivo**
- Un **chat inteligente** con Groq
- Un **procesador automático de Word**
- Un **generador XML Moodle** listo para descargar
- Un **validador de documentos** para detectar errores antes de procesar

---

## 🧠 Funcionalidades principales

### ✔ Conversión automática Word → XML Moodle  
Sube un archivo `.docx` y Hugo:

1. Valida el documento  
2. Limpia el contenido  
3. Detecta preguntas y opciones  
4. Identifica la respuesta correcta  
5. Genera un XML válido para Moodle  
6. Te permite descargarlo al instante  

### ✔ Chat con Hugo  
Puedes hablar con Hugo para:

- Generar preguntas tipo test  
- Resolver dudas  
- Crear contenido educativo  

### ✔ Avatar 3D  
Hugo tiene un modelo 3D interactivo que habla y se mueve.

---

## 📂 Estructura del proyecto


---

## 🚀 Instalación

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py


📄 Requisitos

streamlit
spacy
python-docx
requests
