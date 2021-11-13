import pyttsx3
import PyPDF2 
import os
os.system("cls")

book = open("Scienceofscience.pdf","rb")
readBook = PyPDF2.PdfFileReader(book)
pages = readBook.numPages

speaker = pyttsx3.init()

for i in range(1,pages):
    eachPage = readBook.getPage(i)
    text = eachPage.extractText()
    speaker.say(text)
speaker.runAndWait()
