import json
import re

INPUT_FILE = "data/clean.jsonl"
OUTPUT_FILE = "data/splitted.jsonl"

def classify_line(text):
    if text.endswith("?"):
        return "QUESTION"
    if re.match(r"^[A-D]\)", text):
        return "OPTION"
    return "OTHER"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as inp, \
         open(OUTPUT_FILE, "w", encoding="utf-8") as out:

        for line in inp:
            obj = json.loads(line)
            label = classify_line(obj["text"])
            out.write(json.dumps({"text": obj["text"], "type": label}) + "\n")

if __name__ == "__main__":
    main()

