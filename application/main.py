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
    import glob
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
    import glob
    
Running=False
Webdriver=None #Build autodetect.
Total=0
Failed=0
Passed=0
QuizPin=None
BotsNumber=None
BrowserType=None
GUIText="Welcome To The Quizizz Bot Flood Client..."

def GUI():
    global GUIText
    global Running
    global Webdriver
    global Total
    global Failed
    global Passed
    global QuizPin
    global BotsNumber
    global BrowserType
    root=tkinter.Tk()
    root.minsize(1500,750)
	root.geometry("1500x750")
	root.attributes('-alpha',1)
	#root.iconbitmap('./assets/icon.ico') - Add icon later
	root.configure(bg='black')
	root.title("Quizizz Bot Flooder")
    # Start Functions
    def Exit():
        root.destroy()
		os._exit(1)
    def Update():
        text.set(GUIText)
        root.after(500,Update)
    # End Functions
    # Start Widgets
    text=tkinter.StringVar()
    text.set(GUIText)
    tkinter.Label(root,textvariable=text,fg="#00eaff",bg="#000000",justify="left",anchor="sw",font=("Courier",13)).pack(fill='both',side="left")
    # End Widgets
    Update()
	root.protocol("WM_DELETE_WINDOW",Disable_Close)
	root.mainloop()

interfacethread=threading.Thread(target=GUI)
interfacethread.start()

def setDriver():
    location=os.getcwd()
    fileset=[file for file in glob.glob(location + "**/*.py", recursive=True)]
    for file in fileset:
        if "web" in file.lower() and "driver" in file.lower():
            webdriver_location=file
            break
        else:
            webdriver_location="MicrosoftWebDriver.exe"
        
setDriver()
        
def startBrowser():
    if Webdriver != None:
        if bt.lower() == "c":
            ### .add_argument('headless')
            options=webdriver.ChromeOptions()
            options.use_chromium=True
            options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            browser=webdriver.Chrome(options=options,executable_path=Webdriver)
        else:
            options=EdgeOptions()
            options.use_chromium=True
            options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
            browser=Edge(options=options,executable_path=Webdriver)
    else:
        setDriver()
        startBrowser()

while True:
    if Running:
        pass
