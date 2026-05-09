import asyncio
import edge_tts
import pygame
import os
import uuid

pygame.mixer.init()

async def falar(texto, voz):

    pasta = "audio"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    arquivo = f"audio/{uuid.uuid4()}.mp3"

    tts = edge_tts.Communicate(
        texto,
        voice=voz
    )

    await tts.save(arquivo)

    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    os.remove(arquivo)


def falar_texto(texto, voz):
    asyncio.run(falar(texto, voz))