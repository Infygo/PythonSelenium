from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# handling autosuggest dropdowns
# !! .get_attribute("value") to fetch a text from dynamic text loaded through automation

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
list_countries_elements = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
for country in list_countries_elements:
    if country.text == 'India':
        country.click()
        break
# country_selected = driver.find_element(By.ID, "autosuggest").text -> dynamic text loaded  through automation wont work with .text
country_selected = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print(country_selected)
assert 'India' == country_selected
driver.quit()