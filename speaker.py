import pyttsx3 as pt
import PyPDF2

book=open('ds.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)


speaker=pt.init()
n=int(input('enter the page number'))
page=pdfreader.getPage(128)
text=page.extractText()
speaker.say(text)
# voice=pt.init()
# voice.say('Helo baby girl......darling , i love to the moon and back...............')
# voice.runAndWait()
speaker.runAndWait()

