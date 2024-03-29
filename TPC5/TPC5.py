import json
import re

file_in = open("termos_traduzidos.txt", "r", encoding="utf-8")
linhas = file_in.readlines()
file_in.close()
traducoes = {}
for linha in linhas:
    key, value = linha.split(" @ ")
    value = re.sub(r"\n", "", value)
    traducoes[key] = value

file_in = open("dicionariozinho.json", "r", encoding="utf-8")
dicio = json.load(file_in)
file_in.close()

new_dicio = {}

for designation, description in dicio.items():
    new_dicio[designation] = {
        "des": description,
        "en": traducoes.get(designation)
    }

file_out = open("dicionario_traducao.json", "w", encoding="utf-8")
json.dump(new_dicio, file_out, ensure_ascii=False, indent=4)