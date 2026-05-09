from intents import carregar_intencoes, escolher_idioma
from chatbot import ChatBot

from voices import escolher_voz
from tts import falar_texto


lang = input("Language (pt/en/es/ko): ").lower()
caminho = escolher_idioma(lang)
dados_intencoes = carregar_intencoes(caminho)
bot = ChatBot(dados_intencoes)
usar_voz = input("Enable voice? (y/n): ").lower() == "y"
voz = escolher_voz(lang)


print("\nChatBot started!")
print("Type 'exit' to close.\n")

while True:

    entrada_usuario = input("You: ")

    if entrada_usuario.lower() == "exit":
        print("Bot: See you later!")
        break

    resposta = bot.responder(entrada_usuario)

    print(f"Bot: {resposta}")

    if usar_voz:
        falar_texto(resposta, voz)