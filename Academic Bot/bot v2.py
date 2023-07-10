import openai
import gradio as gr
import speech_recognition as sr
from gtts import gTTS
import tempfile
import pygame

openai.api_key = "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"

messages = [
    {"role": "system", "content": "you are a chemistry professor."},
]

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Sorry, I am facing some technical issues.")
        return ""

def generate_speech(text):
    tts = gTTS(text=text, lang="en")
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts.save(fp.name + ".mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(fp.name + ".mp3")
        pygame.mixer.music.play()

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        generate_speech(reply)
        return reply

def voice_chatbot(query):
    reply = chatbot(query)
    return reply

iface = gr.Interface(fn=voice_chatbot, inputs="microphone", outputs="text",
                     title="Academic Bot", description="Speak anything you want")
iface.launch(share=True)
