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
    box = (Cordinates.dinosaur[0] + 60, Cordinates.dinosaur[1], Cordinates.dinosaur[0] + 100, Cordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())

restartGame()
while True:
    if(image() != 1530):
        pressSpace()
        time.sleep(0.1)


