# Quizizz Bot Flood
A Quizizz bot flood "hack". Tested only on windows.

# How To Use
To use you must download one of the two files, either threaded or not.
[Threaded is in beta and may crash or close for no reason, non-threaded is recommended.]


After downloading the file of your choice you must get the latest edge or chrome web driver, links below:

[Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

[Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)

You must move the web driver exe file into the same folder as the python file, You also need to update the name of the driver inside the python file like so:
```
webdriver_location="<exe_file_name_here>"
```

If you are using chrome instead of edge you also need to change the following lines from:
```
options=EdgeOptions()
options.use_chromium=True
options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
browser=Edge(options=options,executable_path=webdriver_location)
```
To:
```
options=webdriver.ChromeOptions()
options.use_chromium=True
options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
browser=webdriver.Chrome(options=options,executable_path=webdriver_location)
```

# If You Want To Copy
I'm not going to be upset if you copy my code, its open source for a reason. Just give credit where its desired. If you want to work together on a project feel free to reach out to me.
