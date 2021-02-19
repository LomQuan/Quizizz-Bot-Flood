from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
import time
import pyautogui as pya
import keyboard
import random, string

webdriver_location = "MicrosoftWebDriver.exe"
options = EdgeOptions()
options.use_chromium = True
options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe'
browser = Edge(options=options, executable_path=webdriver_location)
qp = input("Quiz Pin: ")
nb = input("Number of Bots: ")
nb = int(nb)

browser.get("https://quizizz.com/join")
pya.moveTo(182, 311)
pya.click()
pya.write(qp, 0.01)
pya.press("enter")
pya.moveTo(486, 452)
pya.click()
pya.moveTo(477, 316)
x = ''.join(random.choice(string.ascii_letters) for _ in range(15))
pya.click()
pya.click()
pya.write(x, 0.01)
pya.press('enter')
nb = nb - 1
while nb != 0:
    pya.keyDown("ctrl")
    pya.press("t")
    pya.keyUp("ctrl")
    pya.write("https://quizizz.com/join", 0.01)
    pya.press("enter")
    time.sleep(1)
    pya.moveTo(182, 311)
    pya.click()
    pya.write(qp, 0.01)
    pya.press("enter")
    pya.moveTo(486, 452)
    pya.click()
    pya.moveTo(477, 316)
    x = ''.join(random.choice(string.ascii_letters) for _ in range(15))
    pya.click()
    pya.click()
    pya.write(x, 0.01)
    pya.press('enter')
    time.sleep(0.5)
    nb = nb - 1
