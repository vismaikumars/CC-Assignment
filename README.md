# Academic Chatbot

This is an academic chatbot powered by OpenAI's GPT-3.5 model. It allows users to have interactive conversations with the chatbot on various academic topics.

## Getting Started

To run the chatbot, you need to have the following dependencies installed:

- Python 3.x
- OpenAI Python library
- Gradio library
- Azure Cognitive Services Speech SDK

You also need to have API keys for OpenAI and Azure Cognitive Services Speech.

### Installation

1. Clone the repository to your local machine

2. Install the required Python packages using pip:

```
pip install openai gradio azure-cognitiveservices-speech
```


3. Replace the placeholder API keys in the code with your own keys:

- `openai.api_key`: Replace `"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"` with your OpenAI API key.
- `speech_key` and `service_region`: Replace the placeholder values with your Azure Cognitive Services Speech API key and service region, respectively.

### Usage

To use the academic chatbot, follow these steps:

1. Run the script:
```
python chatbot.py
```

2. A Gradio interface will open in your default web browser.

3. Enter your queries or messages in the "Chat with AI" text box.

4. Click the "Reply" button or press Enter to get a response from the chatbot.

5. The chat history will be displayed in the interface.

### Speech Recognition

The code also includes functionality for speech recognition using Azure Cognitive Services Speech. To use this feature:

1. Uncomment the code block starting from `async def recognize_speech():` and ending with `await speech_recognizer.recognize_once_async()`.

2. Run the script:


3. Speak into your microphone when prompted.

4. The recognized speech will be printed in the console.

### Speech Synthesis

The code also includes functionality for speech synthesis using Azure Cognitive Services Speech. To use this feature:

1. Uncomment the code block starting from `speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)` and ending with `print(f'Speech synthesized and saved to "{output_file}"')`.

2. Run the script:


3. Enter the text you want to convert to speech when prompted.

4. The synthesized speech will be saved as an audio file named `output.wav` in the current directory.



## Acknowledgments

- This chatbot is powered by the GPT-3.5 model from OpenAI.
- The speech recognition and synthesis capabilities are provided by Azure Cognitive Services Speech SDK.


