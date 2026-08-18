from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://www.saucedemo.com/"
driver.get(base_url)

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

"""INFO PRODUCT 1"""

product1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
valueProduct1 = product1.text
print(valueProduct1)

priceProduct1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
valuePriceProduct1 = priceProduct1.text
print(valuePriceProduct1)

selectProduct1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
selectProduct1.click()
print("Select product 1")

cartButton = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
cartButton.click()
print("Click on cart button")

"""INFO CART PRODUCT 1"""
cartProduct1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
valueCartProduct1 = cartProduct1.text
print(valueCartProduct1)
assert valueProduct1 == valueCartProduct1
print("INFO CART PRODUCT 1 GOOD")

priceCartProduct1 = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']")
valuePriceCartProduct1 = priceCartProduct1.text
print(valuePriceCartProduct1)
assert valuePriceProduct1 == valuePriceCartProduct1
print("INFO PRICE PRODUCT 1 GOOD")

checkoutButton = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkoutButton.click()
print("Click on checkout button")

"""SELECT USER INFO"""
firstNameInput = driver.find_element(By.XPATH, "//input[@id='first-name']")
firstNameInput.send_keys("Alex")
print("Input first name")

lastNameInput = driver.find_element(By.XPATH, "//input[@id='last-name']")
lastNameInput.send_keys("Ivanov")
print("Input last name")

zipInput = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zipInput.send_keys("123456")
print("Input zip code")

continueButton = driver.find_element(By.XPATH, "//input[@id='continue']")
continueButton.click()
print("Click continue button")

"""INFO FINISH PRODUCT 1"""
finishProduct1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
valueFinishProduct1 = finishProduct1.text
print(valueCartProduct1)
assert valueProduct1 == valueFinishProduct1
print("INFO FINISH CART PRODUCT 1 GOOD")

priceFinishProduct1 = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']")
valuePriceFinishProduct1 = priceFinishProduct1.text
print(valuePriceFinishProduct1)
assert valuePriceProduct1 == valuePriceFinishProduct1
print("INFO FINISH PRODUCT 1 GOOD")

summaryPrice = driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']")
valueSummaryPrice = summaryPrice.text
print(valueSummaryPrice)

itemTotal = f"Item total: {valuePriceFinishProduct1}"
assert valueSummaryPrice == itemTotal
print("TOTAL SUMMARY PRICE GOOD")

finishButton = driver.find_element(By.XPATH, "//button[@id='finish']")
finishButton.click()
print("Click on finish button")

orderCompleteHeader = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']")
headerValue = orderCompleteHeader.text
print(headerValue)
assert headerValue == "Thank you for your order!"

backHomeButton = driver.find_element(By.XPATH, "//button[@id='back-to-products']")
backHomeButton.click()
print("Click on back home button")

productHeader = driver.find_element(By.XPATH, "//span[@data-test='title']")
valueProductHeader = productHeader.text
print(valueProductHeader)
assert valueProductHeader == "Products"
