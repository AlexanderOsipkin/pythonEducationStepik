import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://demoqa.com/"
driver.get(base_url + "browser-windows")


"""NEW TAB"""
new_tab = driver.find_element(By.XPATH, "//button[@id='tabButton']")
new_tab.click()
print("Click to the new tab button")
print(driver.current_url)

header_1 = driver.find_element(By.XPATH, "//h1[@class='text-center']")
print(header_1.text)

driver.switch_to.window(driver.window_handles[1])  # отсчет идет с 0, т.е наша демо куа - это 0, новая  -1 и тд
print(driver.current_url)

header_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(header_2.text)

driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)

"""NEW WINDOW"""
new_window = driver.find_element(By.XPATH, "//button[@id='windowButton']")
new_window.click()
print("Click to the new window button")

window_1 = driver.window_handles[0]
window_2 = driver.window_handles[1]

driver.switch_to.window(window_2)
print(driver.current_url)