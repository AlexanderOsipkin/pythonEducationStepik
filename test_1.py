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

textProducts = driver.find_element(By.XPATH, "//span[@class='title']")
vlueTextProducts = textProducts.text  # считываем значение текста в локатаре, запомнили его и сохранили в переменную
print(vlueTextProducts)
assert vlueTextProducts == "Products"
print("Good")

url = "https://www.saucedemo.com/inventory.html"
getUrl = driver.current_url
print(getUrl)
assert url == getUrl
print("Good url")
