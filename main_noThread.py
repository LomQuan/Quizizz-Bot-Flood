try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from msedge.selenium_tools import Edge, EdgeOptions
    import random, string, time, os, socket
except Exception:
    import time, os
    print("-Required packages not installed, installing now...")
    time.sleep(2.5)
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
    import random, string, time, os, socket

webdriver_location="MicrosoftWebDriver.exe"
options=EdgeOptions()
options.use_chromium=True
options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
browser=Edge(options=options,executable_path=webdriver_location)
os.system("cls")
time.sleep(10)
os.system("cls")
failed=0
passed=0
total=0
qp=input("Quiz Pin: ")
nb=input("Number of Bots: ")

try:
    host=socket.gethostbyname("quizizz.com")
    before=time.perf_counter()
    time.sleep(0.25)
    s=socket.create_connection((host, 80), 2)
    after=time.perf_counter()
    pingms=after-before
    pingms=round(pingms, 2)+1
except:
    pingms=2

print("-Calculated action delay: "+str(pingms))

for i in range(int(nb)):
    total=total+1
    passed=passed+1
    try:
        browser.get("https://quizizz.com/join")
        time.sleep(pingms)
        search=browser.find_element_by_class_name("check-room-input")
        search.send_keys(qp)
        search.send_keys(Keys.RETURN)
        print("-Joined Game")
        time.sleep(pingms)
        if browser.find_elements_by_css_selector('.secondary-button.start-over'):
            g=browser.find_elements_by_css_selector('.secondary-button.start-over')
            print("-Start-Over button found")
            g[0].click()
        time.sleep(0.5)
        print("-Entering name option")
        search=browser.find_element_by_class_name("enter-name-field")
        time.sleep(pingms)
        search.send_keys(Keys.CONTROL+"A")
        search.send_keys(''.join(random.choice(string.ascii_letters) for _ in range(10)))
        search.send_keys(Keys.RETURN)
    except (Exception,NoSuchElementException):
        failed=failed+1
        passed=passed-1
    finally:
        time.sleep(pingms)
browser.close()
print("\n\n       Attempted: "+str(total)+" Succeeded: "+str(passed)+" Failed: "+str(failed)+"\n\n\n")
exit()
