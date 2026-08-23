import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://www.saucedemo.com/"
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

dropdown_select = Select(driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']"))
time.sleep(3)
dropdown_select.select_by_visible_text('Name (Z to A)')  # выбор по тексту
time.sleep(3)
dropdown_select.select_by_value('az')  # выбор по value
