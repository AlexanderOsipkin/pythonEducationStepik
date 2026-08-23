import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

# base_url = "https://www.saucedemo.com/"
# driver.get(base_url)
#
# login_standard_user = "standard_user"
# password_all = "secret_sauce"
#
# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# user_name.send_keys(login_standard_user)
# print("Input Login")
#
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print("Input Password")
#
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print("Click login Button")
#
# dropdown_select = Select(driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']"))
# time.sleep(3)
# dropdown_select.select_by_visible_text('Name (Z to A)')  # выбор по тексту
# time.sleep(3)
# dropdown_select.select_by_value('az')  # выбор по value


base_url = "https://www.testmuai.com/selenium-playground/jquery-dropdown-search-demo/"
driver.get(base_url)

time.sleep(2)

click_to_the_dropdown = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_to_the_dropdown.click()

select_country = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[3]")
select_country.click()

time.sleep(2)

click_to_the_dropdown.click()
input_country = driver.find_element(By.XPATH, "(//input[@class='select2-search__field'])[2]")
input_country.send_keys('Hong Kong')

time.sleep(2)

input_country.send_keys(Keys.RETURN)