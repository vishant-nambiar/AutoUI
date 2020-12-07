# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import ctypes
import time
import pyautogui

SendInput = ctypes.windll.user32.SendInput


PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
                        ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#action_hello_world
class ActionHelloWorld(Action):
     def name(self):
      return "action_hello_world"

     def run(self, dispatcher, tracker, domain):
      # last_message = tracker.latest_message.get("text", "")

      

      entities = tracker.latest_message['entities']
      print("Last Message Now ", entities)
     

      for e in entities:
          print(e['entity'])
          if e['entity'] == 'upward':
               print("upward")

               PressKey(0xD0)
               time.sleep(1.5)
               ReleaseKey(0xD0)
                
          elif e['entity'] == 'downward':
              print("downward")
              PressKey(0xC8)
              time.sleep(1.5)
              ReleaseKey(0xC8)
    
          elif e['entity'] == 'leftward':
              print("leftward")
              PressKey(0xCB)
              time.sleep(1.5)
              ReleaseKey(0xCB)

          elif e['entity'] == 'rightward':
              print("rightward")
              PressKey(0xCD)
              time.sleep(1.5)
              ReleaseKey(0xCD)

          elif e['entity'] == 'switch':
      
              PressKey(0xDB)
              ReleaseKey(0xDB)

          elif e['entity'] == 'switch':
            
              PressKey(0x0F)
              ReleaseKey(0x0F)

          elif e['entity'] == 'landgear':
            
              PressKey(0x22)
              ReleaseKey(0x22)

          elif e['entity'] == 'enginedown':
            
              PressKey(0x1E)
              ReleaseKey(0x1E)

            
          elif e['entity'] == 'engineup':
            
              PressKey(0x10)
              ReleaseKey(0x10)
            
          elif e['entity'] == 'brakes':
              PressKey(0x30)
              ReleaseKey(0x30)

          elif e['entity'] == 'brakes':
              PressKey(0x30)
              ReleaseKey(0x30)
                            
          elif e['entity'] == 'screenshot':
              im1 = pyautogui.screenshot()
              im1.save('C:/Users/Rajendra Sarpal/Desktop/game_auto/test.png')

          elif e['entity'] == 'gamequit':
              PressKey(0x38)
              PressKey(0x3E)
              ReleaseKey(0x38)
              ReleaseKey(0x3E)
                
          elif e['entity'] == 'mainmenu':
              PressKey(0x01)
              ReleaseKey(0x01)   
              PressKey(0x01)
              ReleaseKey(0x01)   


            


         
 
      message = "sucess"
      print(message)
      dispatcher.utter_message(text=message)

    
      return []
