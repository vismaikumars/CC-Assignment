# Academic Bot

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


#
#

# Translation Automation with AWS and Google Cloud

This repository contains Python scripts for automating text translation using AWS Translate and Google Cloud Translate services. The scripts are intended to be executed either as standalone Python programs or as AWS Lambda functions. The repository includes two separate scripts, each utilizing a different translation service.

## AWS Translation

The `translateAWS.py` script demonstrates how to translate text stored in an S3 object using the AWS Translate service. The script utilizes the Boto3 library to interact with AWS services, specifically Amazon S3 and Amazon Translate. The translated text is saved back to the S3 bucket for further use.

### Prerequisites

- Python 3.x
- Boto3 library
- AWS CLI configured with appropriate access and secret keys

### Usage

1. Configure AWS CLI with your AWS access and secret keys.
2. Modify the `lambda_handler` function in `aws_translation.py` to customize the translation source and target languages.
3. Execute the script either as a standalone Python program or deploy it as an AWS Lambda function triggered by S3 events.

## Google Cloud Translation

The `translateGCP.py` script demonstrates how to translate text extracted from a PDF file using the Google Cloud Translate API. The script uses the `translate_v2` library from the `google.cloud` package to interact with the Google Cloud Translation service. The translated text is saved to an output file.

### Prerequisites

- Python 3.x
- `google-cloud-translate` library
- Google Cloud Translation API credentials

### Usage

1. Install the `google-cloud-translate` library using pip: `pip install google-cloud-translate`.
2. Obtain the Google Cloud Translation API credentials file in JSON format.
3. Modify the `pdf_filename`, `target_language`, and `output_filename` variables in `google_cloud_translation.py` to match your requirements.
4. Execute the script as a standalone Python program.


#
#

# NLP and Computer Vision 

A Python code that combines Natural Language Processing (NLP) and Computer Vision (CV) using Azure Cognitive Services APIs. This demonstrates how to analyze text sentiment and perform image analysis using Azure Text Analytics and Computer Vision services.

## Prerequisites

- Python 3.x installed on your machine
- Azure subscription with provisioned Cognitive Services resources (Text Analytics and Computer Vision)
- Subscription key and endpoint for Text Analytics and Computer Vision services


## Configuration

1. Open the 'textAndImage.py` file in a text editor or integrated development environment (IDE).

2. Replace the placeholder values `<YOUR_SUBSCRIPTION_KEY>` and `<YOUR_ENDPOINT>` with your actual subscription key and endpoint for both Text Analytics and Computer Vision services.

## Usage

1. Run the Python script by executing the following command in the terminal or command prompt: `python textAndImage.py`
   
2. The script will call the `analyze_text_sentiment` function with an example text and print the sentiment analysis results.

3. It will also call the `analyze_image_objects` function with an example image URL and print the detected objects and tags.

4. Review the output in the terminal or command prompt to see the results of the NLP and CV analysis.


## Disclaimer

Please note that the code provided in this repository is intended for example purposes only. It may require additional error handling, input validation, or modifications to suit your specific use case.




