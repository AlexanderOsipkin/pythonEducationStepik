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

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click login Button")

menu_button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu_button.click()
print("Click menu button")
time.sleep(3)

link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
print("Click link button")


