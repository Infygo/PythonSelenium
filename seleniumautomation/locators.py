# xpath , css , ID, name, linktext, class name
# xpath -> //tagname[@attribute = 'value']
# css -> tagname[attribute = 'value'] -> #idvalue -> .classnamevalue

# .click , .send_keys, .clear, .text

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(options=Options())
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# locators
driver.find_element(By.NAME, "name").send_keys("Vignesh")
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")

driver.find_element(By.CSS_SELECTOR , "input[id='exampleCheck1']").click()

# static dropdowns >> use of Select class
static_dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
static_dropdown.select_by_index(1)
static_dropdown.select_by_visible_text("Male")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("Vignesh2")
driver.find_element(By.XPATH, "(//input[@name='name'])[2]").clear()
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()

success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(success_message)
assert 'Success' in success_message
time.sleep(5)
driver.quit()