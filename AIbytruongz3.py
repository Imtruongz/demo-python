import speech_recognition
import pyttsx3
from datetime import date, datetime
import wikipedia
import webbrowser
import time
import os 

print("AI create by truongz")
truongz_listen = speech_recognition.Recognizer()
while True:
	with speech_recognition.Microphone() as mic:
		audio = truongz_listen.listen(mic)
	print("Truongz:......")
	try:
		me = truongz_listen.recognize_google(audio)
	except:
		me = ""
	print("You: " + me)

	if me == "":
		truongz = "Sorry, I can't hear you, try again"
	elif "YouTube" in me:
		webbrowser.open('https://www.youtube.com',new=2)
		truongz="Ok, Let me"
		truongz_say = pyttsx3.init()
		truongz_say.say(truongz)
		truongz_say.runAndWait()
		break
	
	elif "Facebook" in me:
		webbrowser.open('https://www.facebook.com',new=2)
		truongz="Ok, Let me"
		truongz_say = pyttsx3.init()
		truongz_say.say(truongz)
		truongz_say.runAndWait()
		break
	
	elif "Twitch" in me:
		webbrowser.open('https://www.twitch.tv',new=2)
		truongz="Ok, Let me"
		truongz_say = pyttsx3.init()
		truongz_say.say(truongz)
		truongz_say.runAndWait()
		break
		
	elif "Google" in me:
		webbrowser.open('https://www.google.com',new=2)
		truongz="Ok, Let me"
		truongz_say = pyttsx3.init()
		truongz_say.say(truongz)
		truongz_say.runAndWait()
		break
	elif "hello" in me:
		truongz = "Hi, nice to meet you"

	elif "today" in me:
		today = date.today()
		truongz = today.strftime("%B %d, %Y")
	
	elif "time" in me:
		now = datetime.now()
		truongz = now.strftime("%H hour %M minutes %S seconds")
	
	elif "president" and "America" in me:
		truongz = "Joe Biden is President in America"
	
	elif "Donald Trump" in me:
		truongz = "Donald Trump is former president America"
	
	elif "Joe Biden" in me:
		truongz = "Joe Biden is President in America"

	elif "bye" in me:
		truongz = "Okay, good bye, see you late"
		print("Truongz: " + truongz)
		truongz_say.say(truongz)
		truongz_say.runAndWait()
		break	
	
	else:
		truongz = "I don't know what you say"
	print("Truongz: " + truongz)
	truongz_say = pyttsx3.init()
	truongz_say.say(truongz)
	truongz_say.runAndWait()
	break