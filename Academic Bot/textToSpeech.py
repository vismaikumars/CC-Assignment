import azure.cognitiveservices.speech as speechsdk

speech_key = 'be4c8ee456c941e9b5970d0ef6af90aa'
service_region = 'eastus'  

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# speech synthesizer
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

text_to_speak = input("Enter the text to be converted to speech: ")

# synthesize
result = speech_synthesizer.speak_text_async(text_to_speak).get()


output_file = 'output.wav'
result.audio.write_to_wave_file(output_file)

print(f'Speech synthesized and saved to "{output_file}"')
