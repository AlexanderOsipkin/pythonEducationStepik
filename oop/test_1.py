from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from oop.login_page import LoginPage


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
        login_problem_user = "problem_user"
        password_standard_user = "secret_sauce"

        login = LoginPage(driver)
        login.authorization(login_standard_user, password_standard_user)

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
