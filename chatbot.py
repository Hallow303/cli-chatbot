import random
from intents import detectar_intencao

class ChatBot:
    def __init__(self, dados_intencoes):
        self.dados_intencoes = dados_intencoes

    def responder(self, entrada_usuario):
        intencao, pontuacao = detectar_intencao(
            entrada_usuario,
            self.dados_intencoes
        )

        if pontuacao >= 0.5:
            return random.choice(intencao["responses"]) # type: ignore

        return "I didn't understand."