import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver.switch_to.alert
# alert.accept , alert.dismiss()

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID, "name").send_keys("vignesh")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert_text = driver.switch_to.alert.text
print(alert_text)
assert 'vignesh' in alert_text
time.sleep(5)
driver.switch_to.alert.accept() # accept the alert ok button
# driver.switch_to.alert.dismiss() # cancel/dismiss the alert
