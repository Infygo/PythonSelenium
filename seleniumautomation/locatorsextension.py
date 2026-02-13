from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Xpath and CSS navingating from parent to child
# Xpath -> //parenttag/childtag/childtag > //button[text()='Submit']

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com") #xpath parent child
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("1234") #css parent child element
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("1234") #css using id
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.quit()

