import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# windows_handles > switch_to.window()

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "blinkingText").click()
opened_windows  = driver.window_handles
driver.switch_to.window(opened_windows[1])
email_id = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text.split("@")
user_name = email_id[1].split(".")[0]
print(user_name)
driver.close()
driver.switch_to.window(opened_windows[0])
driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user_name)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys('Learning@830$3mK2')
#driver.find_element(By.CSS_SELECTOR, "#checkMark").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
#time.sleep(10)
explicit_wait = WebDriverWait(driver, 10)
explicit_wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "navbar-brand")))
currentUrl = driver.current_url
print(currentUrl)
assert currentUrl.__contains__("shop")
