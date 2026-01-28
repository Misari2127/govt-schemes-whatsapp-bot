from gtts import gTTS

def text_to_voice(text):
    tts = gTTS(text=text, lang='en')
    filename = "reply.mp3"
    tts.save(filename)
    return filename