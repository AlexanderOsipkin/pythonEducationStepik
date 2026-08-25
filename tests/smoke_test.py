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

"""INFO PRODUCT 2"""

product2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
valueProduct2 = product2.text
print(valueProduct2)

priceProduct2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
valuePriceProduct2 = priceProduct2.text
print(valuePriceProduct2)

selectProduct2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
selectProduct2.click()
print("Select product 2")

"""GO TO CART"""

cartButton = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
cartButton.click()
print("Click on cart button")

"""INFO IN CART PRODUCT 1"""

cartProduct1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
valueCartProduct1 = cartProduct1.text
print(valueCartProduct1)
assert valueProduct1 == valueCartProduct1
print("INFO CART PRODUCT 1 GOOD")

priceCartProduct1 = driver.find_element(By.XPATH,
                                        "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
valuePriceCartProduct1 = priceCartProduct1.text
print(valuePriceCartProduct1)
assert valuePriceProduct1 == valuePriceCartProduct1
print("INFO PRICE PRODUCT 1 GOOD")

"""INFO IN CART PRODUCT 2"""

cartProduct2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
valueCartProduct2 = cartProduct2.text
print(valueCartProduct2)
assert valueProduct2 == valueCartProduct2
print("INFO CART PRODUCT 2 GOOD")

priceCartProduct2 = driver.find_element(By.XPATH,
                                        "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
valuePriceCartProduct2 = priceCartProduct2.text
print(valuePriceCartProduct2)
assert valuePriceProduct2 == valuePriceCartProduct2
print("INFO PRICE PRODUCT 2 GOOD")

"""CLICK TO CHECKOUT BUTTON"""

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

priceFinishProduct1 = driver.find_element(By.XPATH,
                                          "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
valuePriceFinishProduct1 = priceFinishProduct1.text
print(valuePriceFinishProduct1)
assert valuePriceProduct1 == valuePriceFinishProduct1
print("INFO FINISH PRICE PRODUCT 1 GOOD")

"""INFO FINISH PRODUCT 2"""

finishProduct2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
valueFinishProduct2 = finishProduct2.text
print(valueCartProduct2)
assert valueProduct2 == valueFinishProduct2
print("INFO FINISH CART PRODUCT 2 GOOD")

priceFinishProduct2 = driver.find_element(By.XPATH,
                                          "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
valuePriceFinishProduct2 = priceFinishProduct2.text
print(valuePriceFinishProduct2)
assert valuePriceProduct2 == valuePriceFinishProduct2
print("INFO FINISH PRICE PRODUCT 2 GOOD")

"""GET SUMMARY PRICE"""

summaryPrice = driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']")
valueSummaryPrice = summaryPrice.text
print(valueSummaryPrice)

price1 = float(valuePriceFinishProduct1.replace("$", ""))
price2 = float(valuePriceFinishProduct2.replace("$", ""))

totalPrice = price1 + price2

print(f"Total price: ${totalPrice:.2f}")

itemTotal = f"Item total: ${totalPrice:.2f}"
assert valueSummaryPrice == itemTotal
print("TOTAL SUMMARY PRICE GOOD")

"""FINISH BUTTON"""

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
print("TEST PASSED")