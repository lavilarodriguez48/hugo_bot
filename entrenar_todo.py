import os
import subprocess

def run(cmd):
    print(f"\n=== Ejecutando: {cmd} ===\n")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Error ejecutando: {cmd}")
        exit(1)

print("\n🚀 INICIANDO PIPELINE COMPLETO DE ENTRENAMIENTO\n")

# 1. Procesar los Word
run("python scripts/01_extract_paragraphs.py")
run("python scripts/02_clean_paragraphs.py")
run("python scripts/03_split_questions.py")
run("python scripts/04_generate_training_data.py")
run("python scripts/05_convert_to_spacy.py")

# 2. Entrenar el modelo
run("python train_spacy.py")

# 3. (Opcional) Generar Word de salida
if os.path.exists("scripts/generar_words.py"):
    run("python scripts/generar_words.py")

print("\n🎉 ENTRENAMIENTO COMPLETO — MODELO ACTUALIZADO 🎉\n")
