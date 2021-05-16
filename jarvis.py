import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning ")
	elif hour>=12 and hour<18:
		speak("Good AfterNoon ")
	else:
		speak("Good Evening")

	speak("I am Jarvis sir Please tell me How may I help You")

def takeCommand():
	#Its takes microphone input from the user and returns string output

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing......")
		query = r.recognize_google(audio, Language='en-in')
		print(f"user said: {query}\n")

	except Exception as e:
		print(e)
		print("Say That gain please.....")
		return "None"
	return query


if __name__ == '__main__':
	wishMe()
	while True:
		query = takeCommand().lower()
	
	#Logic For Executing Task Based On query

