import itertools
import time
import pyautogui

Alphabet = ("1234567890")
CharLength = 1
for CharLength in range(6,8):
    passwords = (itertools.product(Alphabet, repeat = CharLength))
    for i in passwords:
        i = str(i)
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        pyautogui.keyDown("ctrl")
        pyautogui.press("a")
        pyautogui.keyUp("ctrl")
        pyautogui.typewrite(i)
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")
    CharLength += 1
