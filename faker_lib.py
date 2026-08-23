from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://www.saucedemo.com/"
driver.get(base_url)

faker = Faker("en_US")  # ru_RU - для рандомных джанных на ру языке

name = faker.first_name() + str(faker.random_int())
print(name)

password = faker.password()
print(password)

login_standard_user = name
password_all = password

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
