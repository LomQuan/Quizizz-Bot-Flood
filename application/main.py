try:
    import tkinter
    import random, string, time, os, socket, threading
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from msedge.selenium_tools import Edge, EdgeOptions
except Exception:
    import random, string, time, os, socket, threading
    print("-Required packages not installed, installing now...")
    os.system("pip install selenium")
    os.system("pip install msedge-selenium-tools")
    time.sleep(1)
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from msedge.selenium_tools import Edge, EdgeOptions
    import tkinter
    
Running=False
Webdriver="" #Build autodetect.
Total=0
Failed=0
Passed=0
QuizPin=None
BotsNumber=None
BrowserType=None

def GUI():
    global Running
    global Webdriver
    global Total
    global Failed
    global Passed
    global QuizPin
    global BotsNumber
    global BrowserType

interfacethread=threading.Thread(target=GUI)
interfacethread.start()
