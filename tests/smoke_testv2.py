from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://www.saucedemo.com/"
driver.get(base_url)

# АВТОРИЗАЦИЯ ПОЛЬЗОВАТЕЛЯ ДО ВЫБОРА ТОВАРА
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

# СТАРТОВОЕ СООБЩЕНИЕ И ВЫБОР ТОВАРА ПОЛЬЗОВАТЕЛЕМ
print("Приветствую тебя в нашем интернет-магазине")
print("Выбери один из следующих товаров и укажи его номер:\n"
      "1 - Sauce Labs Backpack\n"
      "2 - Sauce Labs Bike Light\n"
      "3 - Sauce Labs Bolt T-Shirt\n"
      "4 - Sauce Labs Fleece Jacket\n"
      "5 - Sauce Labs Onesie\n"
      "6 - Test.allTheThings() T-Shirt (Red)"
      )

product = int(input())
print("Выбран товар:", product)

# ПРОВЕРЯЕМ НАЛИЧИЕ ТОВАРА В СПИСКЕ
if product < 1 or product > 6:
    print("Неверный номер товара")
    driver.quit()
    exit()

# ИНФОРМАЦИЯ О ПРОДУКТЕ КОТОРЫЙ ВЫБРАЛ ПОЛЬЗОВАТЕЛЬ
product_title = driver.find_element(By.XPATH, f"(//a[contains(@id, 'title_link')])[{product}]")
value_product = product_title.text
print("Название товара:", value_product)

# НАХОДИМ ЦЕНУ ВЫБРАНОГО ТОВАРА ПОЛЬЗОВАТЕЛЕМ
product_price = driver.find_element(By.XPATH, f"(//div[@data-test='inventory-item-price'])[{product}]")
value_price_product = product_price.text
print("Цена товара:", value_price_product)

# ДОБОВЛЯЕМ ТОВАР В КОРЗИНУ
select_product = driver.find_element(By.XPATH, f"(//button[starts-with(@id, 'add-to-cart')])[{product}]")
select_product.click()
print("Товар добавлен в корзину")

# ПЕРЕХОДИМ В КОРЗИНУ
cart_button = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
cart_button.click()
print("Нажимаем на кнопку корзины")

# ПРОВЕРЯЕМ ИНФОРМАЦИЮ В КОРЗИНЕ
cart_product = driver.find_element(By.XPATH, "//div[@data-test='inventory-item']//a")
value_cart_product = cart_product.text
print("Товар в корзине:", value_cart_product)

assert value_product == value_cart_product
print("Информация в корзине верная")

cart_price = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']")
value_cart_price = cart_price.text
print("Цена в корзине:", value_cart_price)

assert value_price_product == value_cart_price
print("Информация о цене верная")

# ЧЕКАУТ
checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print("Нажимаем на кнопку чекаут")

# ВВОДИМ ИНФОРМАЦИЮ О ПОЛЬЗОВАТЕЛЕ
first_name_input = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name_input.send_keys("Alex")
print("Ввели имя пользователя")

last_name_input = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name_input.send_keys("Ivanov")
print("Ввели фамилию пользователя")

zip_input = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_input.send_keys("123456")
print("Ввели зип-код")

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Нажали на кнопку перехода к следующему экрану")

# ФИНАЛЬНАЯ ИНФОРМАЦИЯ О ПРОДУКТЕ
finish_product = driver.find_element(By.XPATH, "//div[@data-test='inventory-item']//a")
value_finish_product = finish_product.text
print("Товар на странице оплаты:", value_finish_product)

assert value_product == value_finish_product
print("Финишная информация о продукте верная")

finish_price = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']")
value_finish_price = finish_price.text
print("Цена на странице оплаты:", value_finish_price)

assert value_price_product == value_finish_price
print("Финишная цена продукта верная")

# SUMMARY PRICE
summary_price = driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']")
value_summary_price = summary_price.text
print(value_summary_price)

item_total = f"Item total: {value_finish_price}"

assert value_summary_price == item_total
print("Общая цена верная")

# ОФОРМЛЯЕМ ЗАКАЗ
finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
finish_button.click()
print("Нажимаем на кнопку финиш")

# ПРОВЕРЯЕМ ЧТО ЗАКАЗ ОФОРМИЛСЯ И ЧТО НАХОДИМСЯ НА ФИНАЛЬНОЙ СТРАНИЦЕ
order_complete_header = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']")
header_value = order_complete_header.text
print(header_value)

assert header_value == "Thank you for your order!"
print("Заказ оформлен")

# ВОЗВРАЩАЕМСЯ НА ГЛАВНУЮ СТРАНИЦУ САЙТА
back_home_button = driver.find_element(By.XPATH, "//button[@id='back-to-products']")
back_home_button.click()
print("Нажимаем на кнопку HOME")

# ПРОВЕРЯЕМ ЧТО ВЕРНУЛИСЬ НА ГЛАВНУЮ СТРАНИЦУ САЙТА
product_header = driver.find_element(By.XPATH, "//span[@data-test='title']")
value_product_header = product_header.text
print(value_product_header)

assert value_product_header == "Products"
print("Тест пройден успешно")
