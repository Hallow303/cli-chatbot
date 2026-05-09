def escolher_voz(lang: str):

    vozes = {
        "pt": "pt-BR-AntonioNeural",
        "en": "en-US-GuyNeural",
        "es": "es-ES-AlvaroNeural",
        "ko": "ko-KR-InJoonNeural"
    }

    lang = lang.lower().strip()

    return vozes.get(lang, vozes["en"])