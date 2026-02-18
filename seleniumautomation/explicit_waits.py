# explicit wait - 15secs wait specific for an webelement / action instead of using global implicit wait of 15 secs

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)
search_results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

# chaining
for results in search_results:
    results.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
explicitWait = WebDriverWait(driver, 10)
explicitWait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
# driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
codeapplied_text = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(codeapplied_text)
assert codeapplied_text == "Code applied ..!"
