from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (340, 390)
    dinosaur = (171, 395)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
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


def main():
    restartGame()
    while True:
        if(image() != 1530):
            pressSpace()
            time.sleep(0.1)

main()

