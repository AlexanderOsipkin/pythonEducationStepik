import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")
options.add_argument("--guest")
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN)  # имитирует enter
time.sleep(2)

now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")  # задаем переменную с текущим временем
name_screenshot = 'screenshot' + now_date + '.png'  # задаем название для скриншота
driver.save_screenshot(f'./screen/{name_screenshot}') # сохраняем скриншот в нужную папку
