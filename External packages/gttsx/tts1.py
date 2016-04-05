from gtts import gTTS
import pygame
import speech_recognition as sr
import datetime
import os

def speak(text_to_speak):
	tts = gTTS(text=text_to_speak, lang='en')
	tts.save('file.mp3')
	pygame.mixer.init()
	pygame.mixer.music.load('file.mp3')
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	pygame.mixer.music.stop()
	pygame.mixer.quit()
	os.remove('file.mp3')


speak_from_fd('Hey!! This is Jarvis. Tell me what to do')
rec = sr.Recognizer()
with sr.Microphone() as source:
	audio = rec.listen(source)

try:
	text = rec.recognize_google(audio)
	if text == 'hello':
		hour_of_day = datetime.datetime.now().hour
		if hour_of_day < 6 or hour_of_day > 18:
			speak('Good Evening sir!!')
		elif hour_of_day > 12:
			speak('Good Afternoon sir!!')
		else:
			speak('Good Morning sir!!')
	elif text == 'goodbye' or text == 'tata' or text == 'bye':
		speak('Goodbye sir!')
	elif text == 'awesome' or text == 'good' or text == 'welldone':
		speak('Thank you sir!')
except sr.UnknownValueError:
	speak('I dunno what you said')