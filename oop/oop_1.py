from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test1():
    def test_select_product(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--guest")
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
        base_url = "https://www.saucedemo.com/"
        driver.get(base_url)

        print("Start test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_standard_user)
        print("Input Login")

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(password_all)
        print("Input Password")

        button_login = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print("Click login Button")

        select_product = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click select product")

        cart_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-test='shopping-cart-link']")))
        cart_button.click()
        print("Click on cart button")

        success_test = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-test='title']")))
        value_success_test = success_test.text
        assert value_success_test == "Your Cart"
        print("Test passed")