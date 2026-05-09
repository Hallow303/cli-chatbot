## 파이썬 CLI 챗봇

🌐 **언어**

[![Português](https://img.shields.io/badge/Português-green?style=for-the-badge)](README_PT.md)
[![English](https://img.shields.io/badge/English-blue?style=for-the-badge)](/README.md)
[![Español](https://img.shields.io/badge/Español-red?style=for-the-badge)](README_ES.md)

파이썬으로 구축된 간단한 명령줄 챗봇입니다. 이 프로젝트는 사용자가 터미널에서 직접 챗봇과 상호 작용할 수 있도록 하며, 다국어 및 선택적 음성 응답을 지원합니다.

### 기능

*   **다국어 지원**: 포르투갈어, 영어, 스페인어 또는 한국어로 상호 작용합니다.
*   **음성 출력**: 챗봇 응답을 위한 선택적 텍스트 음성 변환 기능.
*   **의도 감지**: 미리 정의된 패턴을 기반으로 사용자 의도를 인식합니다.
*   **구성 가능한 응답**: 감지된 의도에 따라 다양한 응답을 제공합니다.
*   **간단한 CLI**: 사용하기 쉬운 명령줄 인터페이스.

### 작동 방식

챗봇은 JSON 파일에서 의도 데이터를 로드하여 작동하며, 이 파일은 다른 언어에 대한 패턴과 해당 응답을 정의합니다. `difflib.SequenceMatcher`를 사용하여 사용자 입력과 미리 정의된 패턴 간의 유사성을 계산하여 사용자 의도를 감지합니다. 음성 출력을 위해 `edge_tts` 라이브러리를 사용하여 텍스트 응답을 음성으로 변환하고, `pygame.mixer`를 사용하여 재생합니다.

### 사용된 기술

*   **Python 3**
*   **JSON**: 의도 데이터 저장용
*   **`difflib`**: 의도 감지에서 문자열 유사성 계산용
*   **`edge_tts`**: 텍스트 음성 변환용
*   **`pygame`**: 오디오 재생용 (음성 응답)
*   **`asyncio`**: 텍스트 음성 변환의 비동기 작업용
*   **`os`**: 파일 시스템 작업용 (오디오 디렉토리 생성)
*   **`uuid`**: 오디오 파일의 고유 파일명 생성용

### 사용 방법

1.  **저장소 복제:**

    ```bash
    git clone <repository_url>
    ```

2.  **프로젝트 폴더로 이동:**

    ```bash
    cd cli-chatbot
    ```

3.  **종속성 설치:**

    ```bash
    pip install edge-tts pygame
    ```

4.  **프로그램 실행:**

    ```bash
    python main.py
    ```

5.  **챗봇과 상호 작용:**

    언어를 선택하고 음성 출력을 활성화하려면 지침을 따르십시오. 메시지를 입력하고 Enter 키를 누르십시오. 대화를 종료하려면 `exit`를 입력하십시오.

### 목적

이 프로젝트는 다음을 연습하기 위한 학습 목적으로 만들어졌습니다.

*   대화형 명령줄 애플리케이션 구축.
*   구성을 위한 JSON 데이터 작업.
*   자연어 처리 개념 (의도 감지) 구현.
*   텍스트 음성 변환 기능 통합.
*   모듈식 파일로 파이썬 코드 구성.
