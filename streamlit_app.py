import streamlit as st
import spacy

# -----------------------------
# Cargar modelo spaCy
# -----------------------------
@st.cache_resource
def load_model():
    return spacy.load("model/modelo_lauri/model-last")

nlp = load_model()

# -----------------------------
# Configuración de la página
# -----------------------------
st.set_page_config(page_title="Hugo 3D", layout="wide")

st.title("👦 Hugo — Tu asistente 3D inteligente")
st.write("Habla con Hugo, tu asistente que clasifica preguntas usando tu modelo spaCy.")

# -----------------------------
# Avatar 3D
# -----------------------------
avatar_html = """
<script type="module"
        src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
</script>

<div style="width: 100%; height: 500px;">
<model-viewer
    src="https://raw.githubusercontent.com/lavilarodriguez48/hugo_bot/main/assets/hugo.glb"
    alt="Hugo"
    auto-rotate
    camera-controls
    style="width: 100%; height: 500px;"
    orientation="0deg 90deg 0deg">
</model-viewer>
</div>
"""

st.components.v1.html(avatar_html, height=500)

# -----------------------------
# Clasificación con spaCy
# -----------------------------
texto = st.text_area("Escribe una pregunta o una opción:")

if st.button("Clasificar"):
    if texto.strip():
        doc = nlp(texto)
        st.subheader("Resultado:")
        st.json(doc.cats)
    else:
        st.warning("Escribe algo primero.")

