## Chatbot CLI em Python

🌐 **Idiomas**

[![Inglês](https://img.shields.io/badge/English-blue?style=for-the-badge)](/README.md)
[![Espanhol](https://img.shields.io/badge/Español-red?style=for-the-badge)](README_ES.md)
[![Coreano](https://img.shields.io/badge/한국어-purple?style=for-the-badge)](README_KO.md)

Um chatbot simples de linha de comando construído com Python. Este projeto permite que os usuários interajam com um chatbot diretamente do terminal, suportando vários idiomas e respostas de voz opcionais.

### Funcionalidades

*   **Suporte a Múltiplos Idiomas**: Interaja em Português, Inglês, Espanhol ou Coreano.
*   **Saída de Voz**: Funcionalidade opcional de texto-para-voz para as respostas do chatbot.
*   **Detecção de Intenção**: Reconhece as intenções do usuário com base em padrões predefinidos.
*   **Respostas Configuráveis**: Fornece respostas variadas com base nas intenções detectadas.
*   **CLI Simples**: Interface de linha de comando fácil de usar.

### Como Funciona

O chatbot opera carregando dados de intenções de arquivos JSON, que definem padrões e respostas correspondentes para diferentes idiomas. Ele usa o `difflib.SequenceMatcher` para calcular a similaridade entre a entrada do usuário e os padrões predefinidos para detectar a intenção do usuário. Para a saída de voz, a biblioteca `edge_tts` é utilizada para converter as respostas de texto em fala, que é então reproduzida usando `pygame.mixer`.

### Tecnologias Utilizadas

*   **Python 3**
*   **JSON** para armazenar dados de intenções
*   **`difflib`**: Para calcular a similaridade de strings na detecção de intenções
*   **`edge_tts`**: Para conversão de texto em fala
*   **`pygame`**: Para reprodução de áudio (respostas de voz)
*   **`asyncio`**: Para operações assíncronas em texto-para-voz
*   **`os`**: Para operações do sistema de arquivos (criação de diretório de áudio)
*   **`uuid`**: Para gerar nomes de arquivos únicos para arquivos de áudio

### Como Usar

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/Hallow303/cli-chatbot.git
    ```

2.  **Navegue até a pasta do projeto:**

    ```bash
    cd cli-chatbot
    ```

3.  **Instale as dependências:**

    ```bash
    pip install edge-tts pygame
    ```

4.  **Execute o programa:**

    ```bash
    python main.py
    ```

5.  **Interaja com o chatbot:**

    Siga as instruções para escolher um idioma e habilitar a saída de voz. Digite suas mensagens e pressione Enter. Digite `exit` para encerrar a conversa.

### Propósito

Este projeto foi criado como um exercício de aprendizado para praticar:

*   Construção de aplicações interativas de linha de comando.
*   Trabalho com dados JSON para configuração.
*   Implementação de conceitos de processamento de linguagem natural (detecção de intenções).
*   Integração de funcionalidades de texto-para-voz.
*   Organização de código Python em arquivos modulares.
