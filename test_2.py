from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")
options.add_argument("--guest")
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

LoginStandardUser = "standard_use"
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

warningText = driver.find_element(By.XPATH, "//h3[@data-test='error']")
valueWarningText = warningText.text
assert valueWarningText == "Epic sadface: Username and password do not match any user in this service"
print("Good test")
