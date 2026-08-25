from selenium import webdriver
from selenium.webdriver.common.by import By

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

"""INFO PRODUCT 1"""

product1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product1 = product1.text
print(value_product1)

price_product1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product1 = price_product1.text
print(value_price_product1)

select_product1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product1.click()
print("Select product 1")

cart_button = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
cart_button.click()
print("Click on cart button")

"""INFO CART PRODUCT 1"""
cart_product1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product1 = cart_product1.text
print(value_cart_product1)
assert value_product1 == value_cart_product1
print("INFO CART PRODUCT 1 GOOD")

price_cart_product1 = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']")
value_price_cart_product1 = price_cart_product1.text
print(value_price_cart_product1)
assert value_price_product1 == value_price_cart_product1
print("INFO PRICE PRODUCT 1 GOOD")

checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print("Click on checkout button")

"""SELECT USER INFO"""
first_name_input = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name_input.send_keys("Alex")
print("Input first name")

last_name_input = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name_input.send_keys("Ivanov")
print("Input last name")

zip_input = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_input.send_keys("123456")
print("Input zip code")

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Click continue button")

"""INFO FINISH PRODUCT 1"""
finish_product1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product1 = finish_product1.text
print(value_cart_product1)
assert value_product1 == value_finish_product1
print("INFO FINISH CART PRODUCT 1 GOOD")

price_finish_product1 = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']")
value_price_finish_product1 = price_finish_product1.text
print(value_price_finish_product1)
assert value_price_product1 == value_price_finish_product1
print("INFO FINISH PRODUCT 1 GOOD")

summary_price = driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']")
value_summary_price = summary_price.text
print(value_summary_price)

item_total = f"Item total: {value_price_finish_product1}"
assert value_summary_price == item_total
print("TOTAL SUMMARY PRICE GOOD")

finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
finish_button.click()
print("Click on finish button")

order_complete_header = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']")
header_value = order_complete_header.text
print(header_value)
assert header_value == "Thank you for your order!"

back_home_button = driver.find_element(By.XPATH, "//button[@id='back-to-products']")
back_home_button.click()
print("Click on back home button")

product_header = driver.find_element(By.XPATH, "//span[@data-test='title']")
value_product_header = product_header.text
print(value_product_header)
assert value_product_header == "Products"
print("TEST PASSED")
