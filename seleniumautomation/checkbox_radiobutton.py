from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkbox_list:
    if checkbox.get_attribute("value") == 'option2':
        checkbox.click()
        assert checkbox.is_enabled()
        break

time.sleep(3)

radiobutton_list = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
for radioButton in radiobutton_list:
    if(radioButton.get_attribute("value") == 'radio2'):
        radioButton.click()
        assert radioButton.is_selected()
        break

time.sleep(3)
print('checkbox & radiobuttons are selected ')
