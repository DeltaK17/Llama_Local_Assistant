
# Local Mistral Voice Assistant
The "Local Mistral Voice Assistant" project integrates local language models with speech recognition to create an interactive voice-driven AI assistant. It allows users to converse with the AI using natural speech, which is converted to text, processed by the AI, and then spoken back to the user. This project is ideal for developers and enthusiasts interested in building and experimenting with voice interfaces and local AI models.


## Acknowledgements

- **OpenAI**: For providing the powerful language models and API that form the core of the AI assistant.
- **SpeechRecognition**: For the robust speech recognition capabilities that enable capturing and transcribing user speech.
- **pyttsx3**: For providing the text-to-speech engine used to vocalize AI responses.
- **LM Studio**: For enabling local deployment of language models, facilitating offline and private AI interactions.
- **TheBloke**: For the specific model "Mistral-7B-Instruct-v0.1-GGUF" used in this project.
- **Python Community**: For the extensive libraries and resources that make projects like this possible.
- **Open Source Contributors**: For their contributions to the tools and libraries utilized in this project.### Documentation

#### Overview

The "Local Mistral Voice Assistant" project combines local language models, speech recognition, and text-to-speech conversion to create an interactive voice-driven AI assistant. This documentation provides detailed information on setup, usage, and functionality.

#### Setup

1. **Install Required Libraries**:
   - Ensure you have Python installed.
   - Install the required Python libraries:
     ```bash
     pip install openai speechrecognition pyttsx3
     ```

2. **Configure OpenAI API**:
   - Set up your local Mistral model server.
   - Update the API key and base URL in the script:
     ```python
     openai.api_key = "lm-studio"
     openai.api_base = "URL_OF_LM_STUDIO_SERVER"
     ```

#### Functions

**`SpeakText(command: str)`**
- **Purpose**: Converts text to speech and plays it aloud.
- **Parameters**:
  - `command`: The text string to be converted to speech.
- **Usage**:
  ```python
  SpeakText("Hello, how can I assist you today?")
  ```

**`record_text() -> str`**
- **Purpose**: Captures and transcribes user's speech into text.
- **Returns**: The transcribed text from the user's speech.
- **Usage**:
  ```python
  user_input = record_text()
  print(user_input)
  ```

**`send_to_openai(messages: list, model: str) -> str`**
- **Purpose**: Sends a list of messages to the specified OpenAI model and retrieves the AI's response.
- **Parameters**:
  - `messages`: A list of message dictionaries containing roles (`user` or `assistant`) and their corresponding content.
  - `model`: The model identifier for the local language model to be used.
- **Returns**: The AI-generated response text.
- **Usage**:
  ```python
  messages = [{"role": "user", "content": "Hello, AI!"}]
  response = send_to_openai(messages)
  print(response)
  ```

#### Main Loop

The main loop of the script continuously listens for user speech, processes it, and responds using the AI model. It maintains a conversation history to ensure context-aware responses.

**Example**:
```python
messages = []

while True:
    user_text = record_text()
    if user_text:
        messages.append({"role": "user", "content": user_text})
        assistant_response = send_to_openai(messages)
        if assistant_response:
            SpeakText(assistant_response)
            print(assistant_response)
            messages.append({"role": "assistant", "content": assistant_response})
```

#### Additional Notes

- Ensure your microphone and speaker are properly configured for optimal performance.
- Adjust the `model` parameter in the `send_to_openai` function to use different local models as needed.
- Customize the script further based on specific requirements and preferences.



## Installation

To set up the "Local LLaMA Voice Assistant" on your system, follow these steps:

#### 1. Prerequisites

- Ensure you have Python 3.6 or later installed. You can download it from [python.org](https://www.python.org/downloads/).
- Ensure you have a functioning microphone and speakers.

#### 2. Install Required Libraries

Open a terminal or command prompt and run the following commands to install the necessary Python libraries:

```bash
pip install openai speechrecognition pyttsx3
```

#### 3. Configure OpenAI API

Set up your local LLaMA model server and update the API key and base URL in the script.

- Replace `URL_OF_LM_STUDIO_SERVER` with the actual URL of your LM Studio server.

```python
openai.api_key = "lm-studio"
openai.api_base = "URL_OF_LM_STUDIO_SERVER"
```

#### 4. Download the Script

Copy the provided script into a new Python file (e.g., `Mistral_chat.py`):



#### 5. Run the Script

In the terminal or command prompt, navigate to the directory where you saved the script and run:

```bash
python Mistral_chat.py
```

This will start the voice assistant. It will listen for your speech, process it, and respond using the local LLaMA model.

### Troubleshooting

- **Microphone Issues**: Ensure your microphone is correctly set up and configured in your operating system.
- **API Errors**: Verify that the OpenAI API key and base URL are correctly set.
- **Dependencies**: Ensure all required Python libraries are installed without errors.
