import json
import spacy
from spacy.tokens import DocBin

INPUT_FILE = "data/training.jsonl"
OUTPUT_FILE = "data/train.spacy"

LABELS = [
    "QUESTION",
    "OPTION_CORRECT",
    "OPTION_WRONG",
    "TRUE_FALSE",
    "MULTI_CORRECT",
    "OTHER"
]

def main():
    nlp = spacy.blank("es")
    db = DocBin()

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            text = obj["text"]
            label = obj["label"]

            doc = nlp.make_doc(text)

            # Inicializar todas las categorías a 0
            doc.cats = {lbl: 0.0 for lbl in LABELS}

            # Activar la categoría correcta
            if label in LABELS:
                doc.cats[label] = 1.0

            db.add(doc)

    db.to_disk(OUTPUT_FILE)
    print("Archivo spaCy generado:", OUTPUT_FILE)

if __name__ == "__main__":
    main()

