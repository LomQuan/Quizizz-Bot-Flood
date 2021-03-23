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
    # If Error Importing Install Fixes And Run
    os.system("pip install selenium")
    os.system("pip install msedge-selenium-tools")
    time.sleep(0.5)
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from msedge.selenium_tools import Edge, EdgeOptions
    import tkinter
    import glob



# Set Variables
Running=False
Webdriver=None #Build autodetect.
Total=0
Failed=0
Passed=0
QuizPin=None
BotsNumber=None
BrowserType=None
browser=None
pingms=None
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
    root.protocol("WM_DELETE_WINDOW",Exit)
    root.mainloop()



# Start GUI As Thread
interfacethread=threading.Thread(target=GUI)
interfacethread.start()



def display(text:str):
    # Display Text To Interface
    global GUIText
    GUIText=GUIText+"\n"+text



# Set The WebDriver Useing Scan
location=os.getcwd()
fileset=[file for file in glob.glob(location + "**/*.py", recursive=True)]
for file in fileset:
    if "web" in file.lower() and "driver" in file.lower():
        webdriver_location=file
        break
    else:
        webdriver_location="MicrosoftWebDriver.exe"



try:
    host=socket.gethostbyname("quizizz.com")
    before=time.perf_counter()
    time.sleep(0.3)
    s=socket.create_connection((host, 80), 2)
    after=time.perf_counter()
    pingms=after-before
    pingms=round(pingms, 2)+1
except:
    pingms=2
finally:
    display("[$] Calculated Delay: "+str(pingms))



if Webdriver != None:
    # Pick Browser
    if BrowserType.lower() == "c":
        ### .add_argument('headless')
        options=webdriver.ChromeOptions()
        options.use_chromium=True
        options.add_argument('headless')
        options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        browser=webdriver.Chrome(options=options,executable_path=Webdriver)
    else:
        options=EdgeOptions()
        options.use_chromium=True
        options.add_argument('headless')
        options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        browser=Edge(options=options,executable_path=Webdriver)



while True:
    # If Running == True:
    Running=True
    if Running:
        # Set Total Up For This Run
        Total=Total+1
        Passed=Passed+1
        try:
            # Load Website
            browser.get("https://quizizz.com/join")
            time.sleep(pingms)
            # Search For Game Pin Input
            search=browser.find_element_by_class_name("check-room-input")
            search.send_keys(QuizPin)
            search.send_keys(Keys.RETURN)
            display("[$] Joined Game")
            time.sleep(pingms)
            # If Start Over Found, Click It.
            if browser.find_elements_by_css_selector('.secondary-button.start-over'):
                g=browser.find_elements_by_css_selector('.secondary-button.start-over')
                display("[!] Start-Over button found")
                g[0].click()
            time.sleep(0.5)
            display("[$] Entering name option")
            # Find Enter Name Element.
            search=browser.find_element_by_class_name("enter-name-field")
            time.sleep((pingms/2))
            # Delete Current Name And Generate New Name
            search.send_keys(Keys.CONTROL+"A")
            search.send_keys(''.join(random.choice(string.ascii_letters) for _ in range(10)))
            search.send_keys(Keys.RETURN)
        except (Exception,NoSuchElementException):
            # If Failed Remove Passed And Add Failed
            display("[!] Failed Join")
            Failed=Failed+1
            Passed=Passed-1
        finally:
            # Sleep To Not Overload
            time.sleep(pingms)
