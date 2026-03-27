import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[@class='sort-icon sort-descending']").click()
expected_sorted_veggies = ['Almond', 'Apple', 'Banana', 'Beans', 'Brinjal']
browser_sorted_veggies = driver.find_elements(By.XPATH, "//tr/td[1]")
actual_sorted_veggies = []
for veggies in browser_sorted_veggies:
    actual_sorted_veggies.append(veggies.text)

print(actual_sorted_veggies)
assert actual_sorted_veggies == expected_sorted_veggies
