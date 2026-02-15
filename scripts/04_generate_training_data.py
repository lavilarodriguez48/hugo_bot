import json

INPUT_FILE = "data/splitted.jsonl"
OUTPUT_FILE = "data/training.jsonl"

def is_correct_option(obj):
    """Detecta si una opción está marcada como correcta por formato."""
    text = obj["text"]

    # Formatos del Word
    if obj.get("bold"):
        return True
    if obj.get("colored"):
        return True
    if obj.get("highlighted"):
        return True
    if obj.get("underline"):
        return True

    # Símbolos típicos
    if "✔" in text or "✓" in text:
        return True
    if "*" in text:
        return True

    return False

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as inp, \
         open(OUTPUT_FILE, "w", encoding="utf-8") as out:

        for line in inp:
            obj = json.loads(line)
            text = obj["text"]
            type_ = obj["type"]

            # Etiquetas finales
            if type_ == "QUESTION":
                label = "QUESTION"

            elif type_ == "TRUE_FALSE":
                label = "TRUE_FALSE"

            elif type_ == "MULTI_CORRECT":
                label = "MULTI_CORRECT"

            elif type_ == "OPTION":
                if is_correct_option(obj):
                    label = "OPTION_CORRECT"
                else:
                    label = "OPTION_WRONG"

            else:
                label = "OTHER"

            out.write(json.dumps({
                "text": text,
                "label": label
            }) + "\n")

if __name__ == "__main__":
    main()


