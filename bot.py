from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replay = (340, 390)
    dinosaur = (171, 395)


def restart():
    pyautogui.click(Cordinates.replay)

def press():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')
	
def image():           
    box = (Cordinates.dinosaur[0]+10, Cordinates.dinosaur[1]-60, Cordinates.dinosaur[0] + 60, Cordinates.dinosaur[1]+60)
    image = ImageGrab.grab(box)
    a = array(image)
    print(a.sum())
    return(a.sum())

def start():
    restart()
    while True:
        if(image() <= 5290760):
            press()
            time.sleep(0.1)
		
start()		
while True:
	image()