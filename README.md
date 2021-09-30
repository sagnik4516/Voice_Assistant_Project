# Voice Command Driven Web Application

This app basically takes user voice command as input and act to it accordingly by multitasking approach

Running the project locally
Steps to be followed:
Go to the File location in the repository and open two files in your compiler the main python file and the html file.

Setup your virtual environment in the .html file

Install the necessary libraries specified in requirements.txt

They can be installed using the pip install -r requirements.txt command in the terminal.

Finally run the project using coderunner using the python3 extension run ultron.py with debugging mode on in the terminal.

A voice command driven web application will be deployed in the local host server in a new tab in your default browser

## Documentation

Files in the repository:

https://github.com/sagnik4516/Task-/blob/master/Flask_basics/ultron.py
- This is the main python file where we have trained our AI model

https://github.com/sagnik4516/Task-/blob/master/Flask_basics/templates/ultron.html
  - This is the html file where we have designed our web application interface its background color and image along with the texts which are to be shown when the web application is opened

https://github.com/sagnik4516/Task-/blob/master/background.jpg
- This is a random background template we have created for the web application UI

https://github.com/sagnik4516/Task-/blob/master/Screen%20Recording%20of%20the%20Project.mp4
- This is the screen recording sample of our project web application where we have recorded a demo of how the app works

https://github.com/sagnik4516/Task-/blob/master/libraries.txt

 It contains all the necessary libraries required for the project
## Installation

Install ultron by the following libraries and modules

```bash
pip install pyttsx3
pip install smtplib
pip install warnings
pip install speech_recognition
pip install datetime
pip install webbrowser
pip install wikipedia
pip install os
pip install pywhatkit
pip install pyjokes
pip install flask
pip install render_templates
pip install requests, json, sys
```
    ## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Background Color | ![#add8e6](https://via.placeholder.com/10/add8e6?text=+) #add8e6 |
| Page Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Heading Color | ![#FFFFFF](https://via.placeholder.com/10/FFFFFF?text=+) #FFFFFF |
| 
        body {
            background-image: url("https://raw.githubusercontent.com/pik1989/Alexa-FlaskAPI/main/templates/background.JPG");
            background-color: #cccccc;
            height: 755px;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
            position: relative;
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`0e520a8a90ee520085a90c06ab9e275d`

base url: http://api.openweathermap.org/data/2.5/weather?

  
## Deployment

To deploy this project on the local host server

```bash
   http://127.0.0.1:5500/Flask_basics/templates/ultron.html
```

  
![Logo](https://github.com/sagnik4516/Task-/blob/master/Screenshot%20(46).png)

    
## Demo

Link to screen recording demo



  https://github.com/sagnik4516/Task-/blob/master/Screen%20Recording%20of%20the%20Project.mp4
## Running Tests

To run tests, run the following command

```bash
  run_ultron
```

  
## Screenshots

![App Screenshot](https://github.com/sagnik4516/Task-/blob/master/Screenshot%20(46).png)

  
## Tech Stack

**Client:** VsCode, Python3, HTMLCSS

**Server:** Flask

  
## Features

- User Friendly UI
- Live previews
- Fullscreen mode
- Cross platform
- Smooth running API

  
## FAQ

#### Can it do basic things like voice assistant like who are you or tell me a joke?


Answer Yes, Various multitasking operations are inbuit in its UI

#### Can I send my email by just saying, without typing?

Answer Yes ofcourse, this app uses the smtplib library for such operations.

  
