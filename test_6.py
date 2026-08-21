import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")
options.add_argument("--guest")
g = Service()
driver = webdriver.Chrome(options=options, service=g)
driver.set_window_size(1920, 1080)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")

time.sleep(5)
user_name.clear()  # либо использовать .send_keys(Keys.CONTROL + 'a') затем element.send_keys(Keys.BACKSPACE
