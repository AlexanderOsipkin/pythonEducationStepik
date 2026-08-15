import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")
# options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
# userName = driver.find_elements_by_id("user-name")
# userName = driver.find_element(By.ID, "user-name") # ID
# userName = driver.find_element(By.NAME, "user-name") # NAME
# userName = driver.find_element(By.XPATH, "//*[@id='user-name']") # xpath full
# userName = driver.find_element(By.XPATH, "//input[@id='user-name']") # xpath
userName = driver.find_element(By.XPATH, "//input[@data-test='username']") # xpath data-test
# password = driver.find_element(By.CSS_SELECTOR, "[id='password']") #CSS selector
password = driver.find_element(By.CSS_SELECTOR, "#password") #CSS selector
buttonLogin = driver.find_element(By.XPATH, "//input[@value='Login']")

userName.send_keys("standard_user")
password.send_keys("secret_sauce")
buttonLogin.click()


# time.sleep(10)
# driver.close()