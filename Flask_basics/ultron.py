from flask import Flask,render_template,redirect,request
import warnings
warnings.filterwarnings('ignore')


import pyttsx3 #This module helps us to recognize the voice command given by the user and then translates into machine level understanding language and further into text
import speech_recognition as sr #This module helps the machine microphne to record and stimulate the input voice commands given by the user
import datetime #This module helps to give the current date and time of our locality
import wikipedia #This module helps to search the results of the commands given by the user in wikipedia website
import webbrowser #The webbrowser module provides a high-level interface to allow displaying Web-based documents to users. 
import os #The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality.
import smtplib #Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. host − This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. , whatsapp,fb, youtube, gmail
import requests, json , sys #These are the prerequisites for the functioning of the weatherAPI and exiting the system
import pyjokes #It stores various number of jokes of various kinds which are available in this python library
import pywhatkit #IT DOES MULTITASKING AT ONE TIME takes many commands at a time

app = Flask(__name__, template_folder='templates')

# speak function will pronounce the string which is passed to it
def engine_talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


#This function will wish you as per the current time of your locality
print("Initializing Ultron...")
MASTER = ("Sagnik")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        engine_talk("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        engine_talk("Good Afternoon" + MASTER)

    else:
        engine_talk("Good Evening" + MASTER)

    
    engine_talk("I am Ultron. How may I help you?")

#This function will take command from microphone and returns as a string
def user_commands():
    
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold=1
        voice = listener.listen(source)

    try:      
        print("Recognizing...")
        command = listener.recognize_google(voice, language = 'en-in')
        print(f"user said: {command}\n") 
           
    except Exception as e:
        print("Say that again please")
        return "None"
    return command  
            
            
            
 #command for telling the current weather of my locality I have received the API KEY from openweathermap.org          
def weather(city):
    # Enter your API key here 
    api_key = "0e520a8a90ee520085a90c06ab9e275d"
    #How to use api_key, see the below code:
    #api_key = "ABCDE"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Give city name 
    city_name = city
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
        temp_in_celcius = current_temperature - 273.15
        return str(int(temp_in_celcius))
    
#This function will send email via smtplib and os module
def sendEmail(to, content):
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("godbittu2@gmail.com", "Piracey@4516")
    server.sendmail("godbittu2@gmail.com", to, content)
    server.close()    

#Main program starts here
def run_ultron():
    engine_talk("Initializing Ultron...")
    wishMe()
    command = user_commands()
    if 'play a song' in command:
        song = 'Arijit Singh'
        engine_talk('Playing some music')
        print("Playing....")
        pywhatkit.playonyt(song)
    elif 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing....' + song)
        print("Playing....")
        pywhatkit.playonyt(song)     
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine_talk('Current Time is' + time)
    elif 'open Google' in command:
        engine_talk("Opening google")
        webbrowser.open("https://www.google.com")
    elif 'open stack overflow' in command:
        engine_talk("Opening stackoverflow")
        webbrowser.open("https://www.stackoverflow.com")
    elif 'open hotstar' in command:
        engine_talk("Opening hotstar")
        webbrowser.open("https://www.hotstar.com")
    elif 'open YouTube' in command:
        engine_talk("Opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif 'open sub' in command:
        engine_talk("Opening your youtube subscriptions")
        webbrowser.open("https://www.youtube.com/feed/subscriptions")
    elif 'how are you' in command:
        engine_talk("I am absolutely fine, tell me what can i do for you")
    elif 'what is your age' in command:
        engine_talk("I was launched two days ago")
    elif 'open flipkart' in command:
        engine_talk("Opening flipkart")
        webbrowser.open("https://www.flipkart.com")
    elif 'open netflix' in command:
        engine_talk("Opening netflix")
        webbrowser.open("https://www.netflix.com")
        'flipkart' 'hotstar' 'netflix' 'whats your name' 
    elif 'joke' in command:
        get_j = pyjokes.get_joke()
        print(get_j)
        engine_talk(get_j)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        engine_talk(info)
    elif 'weather' in command:
        #engine_talk('Please tell name of the city')
        city = 'Kolkata'
        #city = 'Mumbai'
        engine_talk('The temperature in KolKata is' + weather(city) + 'degree celcius')
    elif 'send my email' in command:
            try :
                engine_talk("What should I say")  
                content = user_commands()
                to = "godbittu2@gmail.com"
                sendEmail(to, content)
                engine_talk("Email has been sent!")
            except Exception as e:
                print(e)
                engine_talk("Sorry my friend Sagnik, the email is not sent")
        
    elif 'stop' in command:
        engine_talk("Good bye")
    else:
        engine_talk("I didn't hear you properly")
        print("I didn't hear you properly")

#Route() decorator in Flask is used to bind URL to the function
@app.route('/') # This means when redirecting to /(home) page, we will be able to see the message in the local host server
def hello():
    return render_template("ultron.html") # It opens the html file as a template when calling the whole process

@app.route("/home")
def home():
    return redirect('/')

@app.route('/',methods=['POST', 'GET'])
def submit():
    while True:
        run_ultron()
    return render_template("ultron.html")
        

if __name__ =="__main__":
    app.run(debug=True)