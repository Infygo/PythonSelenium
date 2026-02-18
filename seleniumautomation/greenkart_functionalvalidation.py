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

# validate the search results are matching with the list
list_berries_expected = ['Cucumber', 'Raspberry', 'Strawberry']
list_berries_actual = []

search_results_names = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
search_results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for results in search_results_names:
    stripped_result = results.text.split("-")
    list_berries_actual.append(stripped_result[0].rstrip())

print(list_berries_actual)
assert list_berries_expected == list_berries_actual


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

# validate the total equals to the Total amount calculated
total_price = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
print('# of price items', len(total_price))
sum = 0
for price in total_price:
    sum += int(price.text)
print('Sum of added items in cart', sum)
total_sum = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert total_sum == sum

# validate Total discounted amount is < TOtal amount
total_after_discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print('Total amount after discount', total_after_discount)
assert total_after_discount < total_sum



