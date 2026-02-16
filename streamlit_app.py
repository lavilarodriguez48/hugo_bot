import streamlit as st
import spacy
from procesar_word import extraer_preguntas  
from generar_xml import generar_xml  
import requests
import json
st.image("assets/hugo_logo.svg", width=200)

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
# Configuración de la página
# -----------------------------
st.set_page_config(
    page_title="Hugo — Asistente 3D",
    page_icon="👨‍🦱",
    layout="wide"
)

# -----------------------------
# Encabezado bonito
# -----------------------------
st.markdown("""
# 👨‍🦱 Hugo — Tu asistente 3D inteligente  
### Habla con Hugo, sube Word o genera XML para Moodle  
""")

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
# SUBIDA DE WORD + GENERAR XML
# -----------------------------
# -----------------------------
# SUBIDA DE WORD + VALIDACIÓN + GENERAR XML
# -----------------------------
from validar_word import validar_word

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
            st.stop()  # Detiene el flujo si hay errores

        # 2) Si no hay errores, extraer preguntas
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






