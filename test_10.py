from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://demoqa.com/"
driver.get(base_url + "radio-button")

radio_button = driver.find_element(By.XPATH, "//input[@id='yesRadio']")
radio_button.click()
