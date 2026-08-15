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

LoginStandardUser = "standard_user"
passwordAll = "secret_sauce"

userName = driver.find_element(By.XPATH, "//input[@id='user-name']")
userName.send_keys(LoginStandardUser)
print("Input Login")
time.sleep(2)
userName.send_keys(Keys.BACKSPACE) #удаляет 1 символ
time.sleep(2)
userName.send_keys(Keys.BACKSPACE)
time.sleep(2)
userName.send_keys("er") #добавляет удаленные символы обратно

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(passwordAll)
print("Input Password")
password.send_keys(Keys.RETURN) #имитирует enter

filter = driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']")
filter.click()
print("Click filter")
time.sleep(2)
filter.send_keys(Keys.DOWN) #Спускается на 1 элемент ниже в фильтре
time.sleep(2)
filter.send_keys(Keys.RETURN)
