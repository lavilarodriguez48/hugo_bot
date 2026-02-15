import json
import re

INPUT_FILE = "data/paragraphs.jsonl"
OUTPUT_FILE = "data/clean.jsonl"

def clean_text(text):
    # Eliminar saltos de línea
    text = text.replace("\n", " ").strip()

    # Quitar espacios múltiples
    text = re.sub(r"\s+", " ", text)

    # Quitar caracteres invisibles o raros
    text = text.replace("\u200b", "")  # zero-width space
    text = text.replace("\ufeff", "")  # BOM
    text = text.replace("\xa0", " ")   # non-breaking space

    return text.strip()

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as inp, \
         open(OUTPUT_FILE, "w", encoding="utf-8") as out:

        for line in inp:
            obj = json.loads(line)

            cleaned = clean_text(obj["text"])

            out.write(json.dumps({
                "text": cleaned,
                "bold": obj.get("bold", False),
                "underline": obj.get("underline", False),
                "highlighted": obj.get("highlighted", False),
                "colored": obj.get("colored", False)
            }) + "\n")

if __name__ == "__main__":
    main()

