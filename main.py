import tkinter as tk
from PIL import ImageTk, Image

def run_project():
    print("Hello, World!")

import requests     #requests: A library that allows the user to send HTTP/1.1 requests using Python.
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
import pyttsx3  #text to speech
import speech_recognition as sr  #speech to text
from decouple import config      #defines the parameters, options, settings and preferences applied to operating systems (OSes), infrastructure devices and applications in an IT context
from datetime import datetime    #manipulate date and time object data
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord,open_Edge,open_diskc,open_diskd,open_diske,open_diskf,open_chrome,open_nptel
from random import choice       #The choice() method returns a randomly selected element from the specified sequence
from utils import opening_text  # utils=collection of small Python functions and classes which make common patterns shorter and easier ,opening_text=text utils
from pprint import pprint       #a utility module that you can use to print data structures in a readable, pretty way

#functions:
# find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message: 
# These are functions defined in the functions module for performing different online operations such as finding your IP address, fetching latest news, fetching random advice or jokes, getting trending movies, 
# getting weather report, playing a YouTube video, searching on Google or Wikipedia, sending an email or a WhatsApp message.

# pyttsx3: A Python library for converting text to speech.

# speech_recognition: A Python library for recognizing speech.

# config: A library for defining parameters, options, settings, and preferences applied to operating systems, infrastructure devices, and applications in an IT context.

# datetime: A module for manipulating date and time object data.

# open_calculator, open_camera, open_cmd, open_notepad, open_discord, open_Edge, open_diskc, open_diskd, open_diske, open_diskf, open_chrome, open_nptel: These are functions defined in the os_ops module for opening different applications on the user's system.

# choice: A function from the random module that returns a randomly selected element from a sequence.

# opening_text: A variable that contains text utilities.

# pprint: A function from the pprint module that can be used to print data structures in a readable, pretty way.


USERNAME = config('USER')       
BOTNAME = config('BOTNAME')

import transformers

from transformers import pipeline


model_checkpoint = "huggingface-course/bert-finetuned-squad"

question_answerer = pipeline("question-answering", model=model_checkpoint)

from googlesearch import search

import requests



from bs4 import BeautifulSoup


import wikipedia

import requests


engine = pyttsx3.init('sapi5')                    # get speech to text from user 

# Set Rate
engine.setProperty('rate', 180)                  #reply assistent speed

# Set Volume leval
engine.setProperty('volume', 1.0)

# Set Voice (male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)           #0=male  ,1=female


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    else:
         speak(f"good evening {USERNAME}")
        
    speak(f"I am {BOTNAME}. How can I help  you?")
    


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()                     #understand human speech & convert speech to text
    with sr.Microphone() as source:         #Get input speech from mic
        print('Listening....')
        r.pause_threshold = 1               #he number of seconds the system will take to recognize the voice after the user has completed their sentence
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')     #convert speech to text using googlr recognizer
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('repeat')
        query = 'None'
    return query



def start_py():

    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'close' in query:
            open_discord()

        elif 'open edge' in query:
            open_Edge()
       
       
        elif 'open c drive' in query:
            open_diskc()


        elif 'open d drive' in query:
            open_diskd()

        elif 'open e drive' in query:
            open_diske()

        elif 'open f drive' in query:
            open_diskf()


        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'open chrome' in query:
            open_chrome()

        elif 'open nptel' in query:
            open_nptel()

        elif 'ip address' in query or'my ip' in query :
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"Result from Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif 'whatsapp ' in query or ' whatsapp message' in query:
            speak(' On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif 'email' in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query or "I need some advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query :
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        else : 

            # Set up the Wikipedia API

            wikipedia.set_lang("en")  # Set the language to English

            # Define the search query

            #query = "what is the valuation of twitter"

            # Perform the Google search

            search_results = search(query, num_results=10)

            # Iterate over the search results and find the first relevant result

            ans = ""

            #define a flag variable for failed search in wikipedia

            flag=0

            # Perform the Wikipedia search and get the summary of the page
            try:

                page = wikipedia.page(query)

                # Extract the article content and preprocess it with BeautifulSoup

                soup = BeautifulSoup(requests.get(page.url).content, features="lxml")

                content = soup.find("div", {"class": "mw-parser-output"})

                doc = content.get_text()

                # Extract the summary text by concatenating the sentences until the summary length is approximately 300 words
                summary = ""

                sentences = doc.split('.')

                for sent in sentences:

                    if len(summary.split()) < 300:
                        summary += sent.strip() + '.'

                    else:
                        break

                # Print the summary

                print(summary)
                
                ans+=summary

            except wikipedia.exceptions.DisambiguationError as e:

                print("The search query is ambiguous. Please refine your search.")

                flag=1

            except wikipedia.exceptions.PageError as e:

                print("The Wikipedia page does not exist.")

                flag=1

            #define a flag variable for failed search in google

            flag1 = 0

            for url in search_results:

                response = requests.get(url)

                soup = BeautifulSoup(response.content, "html.parser")

                paragraphs = soup.find_all("p")

                for p in paragraphs:

                    text = p.get_text()

                    if (len(text.split())>= 50):

                        #print(text)

                        ans+=text

                        break

                # Exit the loop if a relevant result was found

                if len(text.split())>= 50:

                    print(ans)

                    break

            else:

                print("No relevant result found for the query: {}".format(query))

                flag1 = 1



            #if both search fails

            if flag and flag1:

                #final answer

                print("unsuccessful")

                speak("unsuccessful")

            else:

                res = question_answerer(question=query, context=ans)

                print(res)

                #final answer
                
                print(query," refers to ",res['answer'])

                speak(query + " refers to " + res['answer'])

if __name__ == '__main__':
    root = tk.Tk()

    # load the image
    image = Image.open("./img.png")

    # create a PhotoImage object
    photo = ImageTk.PhotoImage(image)

    # create a label with the PhotoImage
    background_label = tk.Label(root, image=photo)
    background_label.pack()

    button = tk.Button(root, text="Run Project", command=start_py)
    button.pack()

    root.mainloop()