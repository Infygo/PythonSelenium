# Execute javascript method > window.scrollTo(0, 500)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# use of javascript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")

