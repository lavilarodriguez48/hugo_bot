import spacy
import json
from xml.etree.ElementTree import Element, SubElement, tostring

MODEL_PATH = "model/modelo_lauri/model-best"
INPUT_FILE = "data/clean.jsonl"
OUTPUT_FILE = "data/output.xml"

def main():
    nlp = spacy.load(MODEL_PATH)
    root = Element("document")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            doc = nlp(obj["text"])
            label = max(doc.cats, key=doc.cats.get)

            item = SubElement(root, "item")
            SubElement(item, "text").text = obj["text"]
            SubElement(item, "label").text = label

    xml_str = tostring(root, encoding="unicode")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(xml_str)

if __name__ == "__main__":
    main()

