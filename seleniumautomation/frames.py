# Frames > embedded html sitting on top of the base html > not part of the page actually
# not local to the base html page > driver wont be having any clue to these frames > drivers wont have access to these embedded frames

# driver.switch_to.frame
# driver.switch_to.default_content

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# switch to iframe
driver.switch_to.frame(driver.find_element(By.ID, "courses-iframe"))
driver.find_element(By.LINK_TEXT, "VIEW ALL COURSES").click()
is_displayed = driver.find_element(By.XPATH, "//h2[text()='Browse products']").is_displayed()
print('Browse products is displayed?:', is_displayed)
driver.switch_to.default_content() # switch to html content
driver.quit()

