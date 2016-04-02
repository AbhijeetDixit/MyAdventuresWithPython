from gtts import gTTS
import pygame
import speech_recognition as sr
import datetime


tts = gTTS(text='Hey!! This is Jarvis. Tell me what to do', lang='en')
tts.save('hello.mp3')
pygame.mixer.init()
pygame.mixer.music.load('hello.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
	continue
rec = sr.Recognizer()
with sr.Microphone() as source:
	audio = rec.listen(source)

try:
	text = rec.recognize_google(audio)
	if text == 'hello':
		hour_of_day = datetime.datetime.now().hour
		if hour_of_day < 6 or hour_of_day > 18:
			tts = gTTS(text='Good Evening sir!!', lang='en')
			tts.save('wish.mp3')
			pygame.mixer.init()
			pygame.mixer.music.load('wish.mp3')
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
		elif hour_of_day > 12:
			tts = gTTS(text='Good Afternoon sir!!', lang='en')
			tts.save('wish.mp3')
			pygame.mixer.init()
			pygame.mixer.music.load('wish.mp3')
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
		else:
			tts = gTTS(text='Good Morning sir!!', lang='en')
			tts.save('wish.mp3')
			pygame.mixer.init()
			pygame.mixer.music.load('wish.mp3')
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
except sr.UnknownValueError:
	tts = gTTS(text='Oops!! I dunno what you said', lang='en')
	tts.save('except.mp3')
	pygame.mixer.init()
	pygame.mixer.music.load('except.mp3')
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue