import os
from gtts import gTTS

# setting the language for the voice
language = "en"

# sample text which needs to be converted
file_text = open("sample_text.txt", "r").read().replace("\n", " ")

speech = gTTS(text=file_text, lang=language, slow=False)

# saving the text as voice
speech.save("voice.mp3")

# play the voice saved
os.system("start voice.mp3")