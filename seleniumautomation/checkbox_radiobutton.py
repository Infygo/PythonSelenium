from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# webelement.get_attribute("value")
# is_enabled
# is_selected
# is_displayed


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")  # Xpath
for checkbox in checkbox_list:
    if checkbox.get_attribute("value") == 'option2':
        checkbox.click()
        assert checkbox.is_enabled()
        break

time.sleep(3)

radiobutton_list = driver.find_elements(By.CSS_SELECTOR, ".radioButton")  # css
for radioButton in radiobutton_list:
    if (radioButton.get_attribute("value") == 'radio2'):
        radioButton.click()
        assert radioButton.is_selected()
        break

time.sleep(3)
print('checkbox & radiobuttons are selected ')

assert driver.find_element(By.ID, "displayed-text").is_displayed()  # assertion
print("Box is visible now ")
driver.find_element(By.ID, "hide-textbox").click()  # above element goes into hiding
assert not driver.find_element(By.ID, "displayed-text").is_displayed()  # negate assertion
print("Box is hidden now")
