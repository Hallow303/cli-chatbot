import json
from difflib import SequenceMatcher


def escolher_idioma(lang: str):

    idiomas = {
        "en": "lang_data/en_data.json",
        "es": "lang_data/es_data.json",
        "pt": "lang_data/pt_data.json",
        "ko": "lang_data/ko_data.json"
    }

    lang = lang.lower().strip()

    return idiomas.get(lang, idiomas["en"])
    
def carregar_intencoes(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def similaridade(texto1, texto2):
    return SequenceMatcher(None, texto1, texto2).ratio()

def detectar_intencao(entrada_usuario, dados_intencoes):
    melhor_intencao = None
    melhor_pontuacao = 0

    for intencao in dados_intencoes["intents"]:
        for padrao in intencao["patterns"]:

            pontuacao = similaridade(
                entrada_usuario.lower(),
                padrao.lower()
            )

            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_intencao = intencao

    return melhor_intencao, melhor_pontuacao