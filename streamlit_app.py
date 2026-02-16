import streamlit as st
import spacy
from extraer_preguntas import extraer_preguntas  
from generar_xml import generar_xml  
from validar_word import validar_word
import requests
import json

# -----------------------------
# Configuración de la página
# -----------------------------
st.set_page_config(
    page_title="Hugo — Asistente 3D",
    page_icon="👨‍🦱",
    layout="wide"
)

# -----------------------------
# CABECERA PROFESIONAL
# -----------------------------
col1, col2, col3 = st.columns([1, 2, 2])

with col1:
    # Mostrar logo SVG como HTML
    with open("assets/hugo_logo.svg", "r") as f:
        svg = f.read()
    st.markdown(svg, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <h1 style='margin-bottom:0;'>🧑‍🦱 Hugo — Tu asistente 3D inteligente</h1>
        <h3 style='margin-top:5px; color:#555;'>Habla con Hugo, sube Word o genera XML para Moodle</h3>
    """, unsafe_allow_html=True)

with col3:
    st.components.v1.html("""
    <script type="module"
        src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
    </script>

    <model-viewer
        src="https://raw.githubusercontent.com/lavilarodriguez48/hugo_bot/main/assets/hugo.glb"
        alt="Hugo"
        auto-rotate
        camera-controls
        style="width: 100%; height: 250px;"
        orientation="0deg 90deg 0deg">
    </model-viewer>
    """, height=250)

# -----------------------------
# Cargar modelo spaCy (solo si lo necesitas)
# -----------------------------
@st.cache_resource
def load_model():
    return spacy.load("model/modelo_lauri/model-last")

nlp = load_model()

# -----------------------------
# Función de chat con Hugo (GROQ)
# -----------------------------
def responder_como_asistente(texto):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Eres Hugo, un asistente amable que ayuda a Laura a generar preguntas tipo test y XML para Moodle."},
            {"role": "user", "content": texto}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    respuesta_json = response.json()

    if "choices" not in respuesta_json:
        return "Error en la API de Groq: " + str(respuesta_json)

    return respuesta_json["choices"][0]["message"]["content"]


# -----------------------------
# Script para animación + voz
# -----------------------------
reactive_animation_and_voice = """
<script>
function animateHugo() {
    const model = document.querySelector("model-viewer");
    if (!model) return;

    model.setAttribute("rotation-per-second", "80deg");
    model.cameraOrbit = "0deg 75deg 1.8m";

    setTimeout(() => {
        model.setAttribute("rotation-per-second", "30deg");
        model.cameraOrbit = "0deg 75deg 2.5m";
    }, 2000);
}

function hugoHabla(texto) {
    const msg = new SpeechSynthesisUtterance(texto);
    msg.lang = "es-ES";
    msg.pitch = 1.1;
    msg.rate = 1;
    speechSynthesis.speak(msg);
}
</script>
"""

st.components.v1.html(reactive_animation_and_voice, height=0)

# -----------------------------
# CHAT CON HUGO
# -----------------------------
with st.container(border=True):
    st.subheader("💬 Habla con Hugo")

    mensaje = st.text_input("Escribe algo para hablar con Hugo:")

    if st.button("Enviar mensaje"):
        if mensaje.strip():
            respuesta = responder_como_asistente(mensaje)

            st.write("### Hugo dice:")
            st.write(respuesta)

            st.components.v1.html(f"<script>hugoHabla('{respuesta}')</script>", height=0)
            st.components.v1.html("<script>animateHugo()</script>", height=0)

# -----------------------------
# SUBIDA DE WORD + VALIDACIÓN + GENERAR XML
# -----------------------------
with st.container(border=True):
    st.subheader("📄 Convertir Word a XML para Moodle")

    archivo = st.file_uploader("Sube un archivo Word (.docx)", type=["docx"])

    if archivo:
        # 1) Validar el documento
        errores = validar_word(archivo)

        if errores:
            st.error("⚠️ Se han encontrado problemas en el documento:")
            for e in errores:
                st.write(f"- {e}")
            st.stop()

        # 2) Extraer preguntas
        preguntas = extraer_preguntas(archivo)

        if not preguntas:
            st.error("No se han podido extraer preguntas válidas del documento.")
        else:
            st.success(f"Se han detectado {len(preguntas)} preguntas correctamente.")
            st.json(preguntas)

            # 3) Generar XML
            xml = generar_xml(preguntas)

            st.download_button(
                "Descargar XML para Moodle",
                xml,
                file_name="preguntas.xml"
            )

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("ℹ️ Información")
    st.markdown("""
    - Procesador de Word → XML  
    - Chat con Hugo  
    - Avatar 3D  
    - Autora: Laura  
    """)





