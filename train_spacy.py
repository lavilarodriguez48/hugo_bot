import spacy
from spacy.cli.train import train

def main():
    train("config.cfg", output_path="model/modelo_lauri")

if __name__ == "__main__":
    main()
