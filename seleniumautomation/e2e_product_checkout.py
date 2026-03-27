from os import wait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# driver & browser instantiation
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")


# element locators
mobile_models = driver.find_elements(By.XPATH, "//div[@class='card h-100']")  # /div/h4
checkout_homepage = driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']")
#checkout2 = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
#country = driver.find_element(By.CSS_SELECTOR, "#country")

mobile_checkoutlist = ['Blackberry', 'iphone X']

# locator chaining
for mobile in mobile_checkoutlist:
    for i in mobile_models:
        if i.find_element(By.XPATH, "div/h4/a").text == mobile:
            i.find_element(By.XPATH, "div[2]/button").click()
checkout_homepage.click()

for phone_model in mobile_checkoutlist:
    assert driver.find_element(By.XPATH, "//a[text()='" + phone_model +"']").is_displayed()
    print("Checkout page has the "+phone_model+ " selected")

explicit_wait = WebDriverWait(driver, 10)
explicit_wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@class='btn btn-success']")))
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

explicit_wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@value='Purchase']")))
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("India")
explicit_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='suggestions']/ul")))
autosuggest_dropdown = driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul")
for country in autosuggest_dropdown:
    if country.text == 'India':
        country.click()
        break
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-pr']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
explicit_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert-success')]")))
assert driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]").is_displayed()
assert driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]").text.__contains__('Success')
print('Checkout is successful')





