from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replay = (340, 390)
    dinosaur = (150, 120)


def restart():
    pyautogui.click(Cordinates.replay)

def press():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')
	
def image():           
    box = (Cordinates.dinosaur[0], Cordinates.dinosaur[1], Cordinates.dinosaur[0]+150, Cordinates.dinosaur[1]+180)
    image = ImageGrab.grab(box)
    #image.show()
    a = array(image)
    print(a.sum())
    return(a.sum())

def start():
    restart()
    while True:
        if(image() <= 20220000):
            press()
            time.sleep(0.1)
		
start()		
#while True:
#image()