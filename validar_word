from docx import Document
import re

def validar_word(docx_file):
    doc = Document(docx_file)
    errores = []
    preguntas_detectadas = 0

    pregunta_regex = r"\s*\d+[\.\)\-\º]\s+"
    opcion_regex = r"\s*[a-dA-D][\)\.\-\:]\s+"

    actual_tiene_opciones = False
    actual_tiene_correcta = False

    for p in doc.paragraphs:
        texto = p.text.strip()

        if re.match(pregunta_regex, texto):
            preguntas_detectadas += 1

            if preguntas_detectadas > 1:
                if not actual_tiene_opciones:
                    errores.append(f"La pregunta {preguntas_detectadas-1} no tiene opciones.")
                if not actual_tiene_correcta:
                    errores.append(f"La pregunta {preguntas_detectadas-1} no tiene respuesta correcta detectada.")

            actual_tiene_opciones = False
            actual_tiene_correcta = False

        elif re.match(opcion_regex, texto):
            actual_tiene_opciones = True

            for run in p.runs:
                if run.bold or run.underline or run.font.highlight_color or (run.font.color and run.font.color.rgb):
                    actual_tiene_correcta = True

    if preguntas_detectadas > 0:
        if not actual_tiene_opciones:
            errores.append(f"La última pregunta no tiene opciones.")
        if not actual_tiene_correcta:
            errores.append(f"La última pregunta no tiene respuesta correcta detectada.")

    if preguntas_detectadas == 0:
        errores.append("No se han detectado preguntas en el documento.")

    return errores
