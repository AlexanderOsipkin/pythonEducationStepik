from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")  # запускаем тест без открытия браузера
options.add_argument("--guest")
# options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
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

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click login Button")

text_products = driver.find_element(By.XPATH, "//span[@class='title']")
vlue_text_products = text_products.text  # считываем значение текста в локатаре, запомнили его и сохранили в переменную
print(vlue_text_products)
assert vlue_text_products == "Products"
print("Good")

url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print(get_url)
assert url == get_url
print("Good url")
