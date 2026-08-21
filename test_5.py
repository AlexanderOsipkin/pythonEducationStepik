import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

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

driver.execute_script("window.scrollTo(0, 200)")  # скролл экрана по Х и Y на определенное количество пикселей, -200 - это вверх, 200 - вниз
action = ActionChains(driver)  # заводим переменную
white_tshirt_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(white_tshirt_button).perform()  # перемещаемся к указанному элементу на экране

time.sleep(5)

now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")  # задаем переменную с текущим временем
name_screenshot = 'screenshot' + now_date + '.png'  # задаем название для скриншота
driver.save_screenshot(f'./screen/{name_screenshot}')  # сохраняем скриншот в нужную папку
print("Скриншот сохранен")
