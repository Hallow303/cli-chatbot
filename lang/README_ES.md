## Chatbot CLI en Python

🌐 **Idiomas**

[![Português](https://img.shields.io/badge/Português-green?style=for-the-badge)](README_PT.md)
[![Inglês](https://img.shields.io/badge/English-blue?style=for-the-badge)](/README.md)
[![Coreano](https://img.shields.io/badge/한국어-purple?style=for-the-badge)](README_KO.md)

Un chatbot simple de línea de comandos construido con Python. Este proyecto permite a los usuarios interactuar con un chatbot directamente desde la terminal, soportando múltiples idiomas y respuestas de voz opcionales.

### Características

*   **Soporte Multilingüe**: Interactúa en portugués, inglés, español o coreano.
*   **Salida de Voz**: Funcionalidad opcional de texto a voz para las respuestas del chatbot.
*   **Detección de Intenciones**: Reconoce las intenciones del usuario basándose en patrones predefinidos.
*   **Respuestas Configurables**: Proporciona respuestas variadas basadas en las intenciones detectadas.
*   **CLI Simple**: Interfaz de línea de comandos fácil de usar.

### Cómo Funciona

El chatbot opera cargando datos de intenciones de archivos JSON, que definen patrones y respuestas correspondientes para diferentes idiomas. Utiliza `difflib.SequenceMatcher` para calcular la similitud entre la entrada del usuario y los patrones predefinidos para detectar la intención del usuario. Para la salida de voz, se utiliza la biblioteca `edge_tts` para convertir las respuestas de texto en voz, que luego se reproduce usando `pygame.mixer`.

### Tecnologías Utilizadas

*   **Python 3**
*   **JSON** para almacenar datos de intenciones
*   **`difflib`**: Para calcular la similitud de cadenas en la detección de intenciones
*   **`edge_tts`**: Para la conversión de texto a voz
*   **`pygame`**: Para la reproducción de audio (respuestas de voz)
*   **`asyncio`**: Para operaciones asíncronas en texto a voz
*   **`os`**: Para operaciones del sistema de archivos (creación de directorio de audio)
*   **`uuid`**: Para generar nombres de archivo únicos para archivos de audio

### Cómo Usar

1.  **Clona el repositorio:**

    ```bash
    git clone <repository_url>
    ```

2.  **Navega a la carpeta del proyecto:**

    ```bash
    cd cli-chatbot
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install edge-tts pygame
    ```

4.  **Ejecuta el programa:**

    ```bash
    python main.py
    ```

5.  **Interactúa con el chatbot:**

    Sigue las indicaciones para elegir un idioma y habilitar la salida de voz. Escribe tus mensajes y presiona Enter. Escribe `exit` para finalizar la conversación.

### Propósito

Este proyecto fue creado como un ejercicio de aprendizaje para practicar:

*   Construcción de aplicaciones interactivas de línea de comandos.
*   Trabajo con datos JSON para configuración.
*   Implementación de conceptos de procesamiento de lenguaje natural (detección de intenciones).
*   Integración de funcionalidades de texto a voz.
*   Organización de código Python en archivos modulares.
