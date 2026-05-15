import speech_recognition as sr


def listen_to_voice(timeout=5, phrase_time_limit=5):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

        transcription = recognizer.recognize_google(audio)
        return True, transcription
    except Exception as exc:
        return False, str(exc)
