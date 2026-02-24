import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# ActionChains(driver) > performs mouse actions

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
mouse_actions = ActionChains(driver)
mouse_actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# mouse_actions.context_click() # right click
# mouse_actions.double_click() # double click
mouse_actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(3)