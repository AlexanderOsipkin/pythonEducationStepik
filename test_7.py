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

LoginStandardUser = "standard_user"
passwordAll = "secret_sauce"

userName = driver.find_element(By.XPATH, "//input[@id='user-name']")
userName.send_keys(LoginStandardUser)
print("Input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(passwordAll)
print("Input Password")

buttonLogin = driver.find_element(By.XPATH, "//input[@id='login-button']")
buttonLogin.click()
print("Click login Button")

menuButton = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menuButton.click()
print("Click menu button")
time.sleep(3)

linkAbout = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
linkAbout.click()
print("Click link button")


