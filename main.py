import time
from datetime import datetime
from pynput.keyboard import Key, Controller
from data import list
import webbrowser
keyboard = Controller()
isStarted = False
for i in list:
    while True:
        if isStarted == False :
            if datetime.now().hour == int(i[1].split(":")[0]) and datetime.now().minute == int(i[1].split(":")[1]) :
                webbrowser.open(i[0])
                print(i[0],end="\t")
                print(datetime.now())
                isStarted = True
        elif isStarted == True :
            if datetime.now().hour == int(i[2].split(":")[0]) and datetime.now().minute == int(i[2].split(":")[1]):
                isStarted = False
                keyboard.press('q')
                time.sleep(2)
                keyboard.press(Key.enter)
                break