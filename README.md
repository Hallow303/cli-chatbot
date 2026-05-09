## CLI Chatbot in Python

🌐 **Languages**

[![Português](https://img.shields.io/badge/Português-green?style=for-the-badge)](lang/README_PT.md)
[![Español](https://img.shields.io/badge/Español-red?style=for-the-badge)](lang/README_ES.md)
[![한국어](https://img.shields.io/badge/한국어-purple?style=for-the-badge)](lang/README_KO.md)

A simple command-line chatbot built with Python. This project allows users to interact with a chatbot directly from the terminal, supporting multiple languages and optional voice responses.

### Features

*   **Multi-language Support**: Interact in Portuguese, English, Spanish, or Korean.
*   **Voice Output**: Optional text-to-speech functionality for chatbot responses.
*   **Intent Detection**: Recognizes user intentions based on predefined patterns.
*   **Configurable Responses**: Provides varied responses based on detected intents.
*   **Simple CLI**: Easy-to-use command-line interface.

### How it works

The chatbot operates by loading intent data from JSON files, which define patterns and corresponding responses for different languages. It uses the `difflib.SequenceMatcher` to calculate the similarity between user input and predefined patterns to detect the user's intention. For voice output, the `edge_tts` library is utilized to convert text responses into speech, which is then played using `pygame.mixer`.

### Technologies Used

*   **Python 3**
*   **JSON** for storing intent data
*   **`difflib`**: For calculating string similarity in intent detection
*   **`edge_tts`**: For text-to-speech conversion
*   **`pygame`**: For playing audio (voice responses)
*   **`asyncio`**: For asynchronous operations in text-to-speech
*   **`os`**: For file system operations (creating audio directory)
*   **`uuid`**: For generating unique filenames for audio files

### How to Use

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Hallow303/cli-chatbot.git
    ```

2.  **Navigate to the project folder:**

    ```bash
    cd cli-chatbot
    ```

3.  **Install dependencies:**

    ```bash
    pip install edge-tts pygame
    ```

4.  **Run the program:**

    ```bash
    python main.py
    ```

5.  **Interact with the chatbot:**

    Follow the prompts to choose a language and enable voice output. Type your messages and press Enter. Type `exit` to end the conversation.

### Purpose

This project was created as a learning exercise to practice:

*   Building interactive command-line applications.
*   Working with JSON data for configuration.
*   Implementing natural language processing concepts (intent detection).
*   Integrating text-to-speech functionalities.
*   Organizing Python code into modular files.
