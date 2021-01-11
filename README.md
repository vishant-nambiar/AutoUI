# Prototype Submission for EY GDS Hackathon

## Theme - Voice User Interface for Gaming Solution

## Frameworks/Libraries/Open Source Used:

* Pyautogui
* RASA
* ctypes
* time
* requests
* json
* speech recognition
* subprocess
* openvino
* opencv
* numpy
* os
* logging
* math


## RASA(NLP)

* White Space Tokenizer
* Regex Featurizer
* Lexical Syntactic Featurizer
* Count Vectors Featurizer
* DIET Classifier

## Computer Vision
* OpenVino
* OpenCV

## Steps to Run
* Download & Open 'Extreme landings' Game from Windows Store
* Install all the dependencies
* If training for new data:
    * Command - 'rasa train'    (Core Training)
    * Command - 'rasa train nlu' (Data Training)
* Run this command for RASA server:
   'rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml'
* For Action server:
   'rasa run actions'
* For Voice Input:
   'python Voice_bot.py'
   
   
* Try with custom Voice input to play the game and System navigation





### Team - sarpal465_37eb
### Mentor: Mr. Imtiyaz Inamdar
### Members:
* Rajendra Sarpal(AI/ML)
* Vishant Nambiar(Web Developer)
