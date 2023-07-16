# text sentiment and image analysis
import os
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from azure.cognitiveservices.language.textanalytics.models import TextDocumentInput
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes


subscription_key = '<YOUR_SUBSCRIPTION_KEY>'
endpoint = '<YOUR_ENDPOINT>'


text_client = TextAnalyticsClient(endpoint=endpoint, credential=subscription_key)


vision_client = ComputerVisionClient(endpoint=endpoint, credentials=subscription_key)


def analyze_text_sentiment(text):
    documents = [TextDocumentInput(id='1', text=text)]
    response = text_client.sentiment(documents=documents)

    sentiment_score = response.documents[0].score
    sentiment_label = 'Positive' if sentiment_score >= 0.5 else 'Negative'

    print(f'Text Sentiment: {sentiment_label} (Score: {sentiment_score})')


def analyze_image_objects(image_url):
    response = vision_client.analyze_image(image_url, visual_features=[VisualFeatureTypes.objects])

    if response.objects:
        print('Detected Objects:')
        for obj in response.objects:
            print(f'\t- {obj.object_property} ({obj.confidence * 100:.2f}%)')
    else:
        print('No objects detected.')


text = 'I am feeling great today!'
image_url = 'https://parade.com/1161189/alexandra-hurtado/star-wars-trivia/'

analyze_text_sentiment(text)
analyze_image_objects(image_url)
