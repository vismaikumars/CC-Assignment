import asyncio
import azure.cognitiveservices.speech as speechsdk

speech_key = 'be4c8ee456c941e9b5970d0ef6af90aa'
service_region = 'eastus'

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

async def recognize_speech():
    print('Speak into your microphone...')
    done = False

    def stop_cb(evt):
        nonlocal done
        print('Speech recognition stopped.')
        done = True

    speech_recognizer.recognizing.connect(lambda evt: print('Recognizing:', evt.result.text))
    speech_recognizer.recognized.connect(lambda evt: print('Recognized:', evt.result.text))
    speech_recognizer.session_started.connect(lambda evt: print('Session started.'))
    speech_recognizer.session_stopped.connect(lambda evt: print('Session stopped.'))

    speech_recognizer.start_continuous_recognition()
    
    while not done:
        await asyncio.sleep(0.1)

    speech_recognizer.stop_continuous_recognition()
    await speech_recognizer.recognize_once_async()  # Process any remaining speech

async def main():
    await recognize_speech()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())