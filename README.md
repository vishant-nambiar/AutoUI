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
* For Eye Tracker:
 - Navigate to directory/src
 - Run the following command: "python main.py -fdm "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\face-detection-adas-binary-0001\FP32-INT1\face-detection-adas-binary-0001" -flm "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\landmarks-regression-retail-0009\FP16\landmarks-regression-retail-0009" -hpm "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\head-pose-estimation-adas-0001\FP16\head-pose-estimation-adas-0001" -gem "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\gaze-estimation-adas-0002\FP16\gaze-estimation-adas-0002" -i "C:\Users\Rajendra Sarpal\Desktop\Computer-Pointer-Controller\bin\demo.mp4" -d CPU"

 - For Webcam Input: "python main.py -fdm "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\face-detection-adas-binary-0001\FP32-INT1\face-detection-adas-binary-0001" -flm "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\landmarks-regression-retail-0009\FP16\landmarks-regression-retail-0009" -hpm "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\head-pose-estimation-adas-0001\FP16\head-pose-estimation-adas-0001" -gem "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\gaze-estimation-adas-0002\FP16\gaze-estimation-adas-0002" -i cam -d CPU
 
 * For Custom Object Tracking:
   'python color.py'
   'python test.py'
   
   
* Try with custom Voice input to play the game and System navigation





### Team - sarpal465_37eb
### Mentor: Mr. Imtiyaz Inamdar
### Members:
* Rajendra Sarpal
* Vishant Nambiar
