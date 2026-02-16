from docx import Document

def extraer_preguntas(docx_file):
    doc = Document(docx_file)
    preguntas = []
    pregunta_actual = {"pregunta": "", "opciones": [], "correcta": None}

    for p in doc.paragraphs:
        texto = p.text.strip()

        if texto.startswith("P:"):
            if pregunta_actual["pregunta"]:
                preguntas.append(pregunta_actual)
                pregunta_actual = {"pregunta": "", "opciones": [], "correcta": None}
            pregunta_actual["pregunta"] = texto[2:].strip()

        elif texto.startswith("A:"):
            pregunta_actual["opciones"].append(texto[2:].strip())

        elif texto.startswith("C:"):
            pregunta_actual["correcta"] = texto[2:].strip()

    if pregunta_actual["pregunta"]:
        preguntas.append(pregunta_actual)

    return preguntas
