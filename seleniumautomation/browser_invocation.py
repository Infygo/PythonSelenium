# webdriver > chromedriver > chrome browser automation
# get method > hit url
# sleep method > waits

from selenium import webdriver # webdriver from selenium
import time

# service class
from selenium.webdriver.firefox.service import  Service # firefox service class
from selenium.webdriver.chrome.service import Service # chrome service class
from selenium.webdriver.edge.service import Service # edge service class

# options
from selenium.webdriver.chrome.options import Options # chrome options
# from selenium.webdriver.firefox.options import Options # firefox options

from webdriver_manager.chrome import ChromeDriverManager # chromedriver manager

# option 1 direct straightforward
# driver = webdriver.Chrome()

#option 2 chatgpt one
options = Options()
options.add_argument("--start-maximized")

# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()),
#     options=options
# )

#option 3 udemy when chrome version is outdate needs to download chromedriver as service class
# service_obj_chrome = Service("/home/vig/Desktop/PythonSelenium/chromedriver-linux64/chromedriver")
# service_obj_firefox = Service("/home/vig/Desktop/PythonSelenium/geckodriver-v0.36.0-linux64/geckodriver")
# driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Firefox(service=service_obj_firefox)


driver = webdriver.Chrome(options=options)
#driver = webdriver.Firefox(options=options)
driver.get("https://rahulshettyacademy.com")
print(driver.title)
time.sleep(5)
driver.quit()
