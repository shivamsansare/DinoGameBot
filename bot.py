import pyautogui
import time

class Cordinates():
    replay = (480, 400)
    dinosaur = (246, 405)

def restart():
    pyautogui.click(Cordinates.replay)

def space():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')


restart()
while True:
    space()
    time.sleep(0.05)
