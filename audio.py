# from pypdf import PdfReader
# from gtts import gTTS
# tts = gTTS("Hello",lang='en')
# tts.save("demo.mp3")


from pypdf import PdfReader
from gtts import gTTS 

text = ""

reader = PdfReader("operators_task-2-1-1.pdf")

for page in reader.pages:
    text += page.extract_text()


tts = gTTS(text=text,lang='en')

tts.save("operators.mp3")