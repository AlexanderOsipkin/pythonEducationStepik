import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://demoqa.com/"
driver.get(base_url + "buttons")

action = ActionChains(driver)

double_click = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click).perform()

right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click).perform()
