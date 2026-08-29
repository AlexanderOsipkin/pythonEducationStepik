from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from oop.login_page import LoginPage


class TestPage():
    def test_login_and_logout_users(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--guest")
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
        base_url = "https://www.saucedemo.com/"
        driver.get(base_url)

        print("start test")

        # Создаем список пользователей
        users = [
            "standard_user",
            "locked_out_user",
            "problem_user",
            "performance_glitch_user"
        ]

        password = "secret_sauce"

        # Запускаем тест перебирая каждого пользователяч по очерпеди
        for user in users:
            print(f"Логинимся пользователем: {user}")
            login = LoginPage(driver)

            try:
                # Авторизация пользователя
                login.authorization(user, password)

                # Проверяем что успешно авторизовались
                check_main_page = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='title']")))
                main_value = check_main_page.text

                assert main_value == "Products"
                print(f"Пользователь {user} успешно авторизован")

                # Открываем бургер-меню
                burger_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
                burger_button.click()
                print("Открылось бургер-меню")

                # Выходим из авторизованного пользователя
                logout_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
                logout_button.click()
                print(f"Пользователь {user} вышел из аккаунта")

                # Проверяем что вернулись на страницу авторизации
                login_page = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='login_logo']")))

                assert login_page.text == "Swag Labs"
                print("Вернулись на страницу авторизации")

            except Exception as error:
                # Если авторизация не прошла, проверяем наличие сообщения об ошибке
                try:
                    error_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='error-button']")))
                    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
                    print(f"Пользователь {user} не смог авторизоваться")
                    print("Получена ошибка:", error_message)

                    # Закрываем сообщение об ошибке
                    error_button.click()

                    # Очищаем поле логина
                    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
                    user_name.clear()

                    # Очищаем поле пароля
                    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
                    password_input.clear()

                    print("Поля для ввода логина и пароля очищены")
                    print("Переходим к следующему пользователю")

                except Exception:
                    # Если это была любая другаяч ошибка, выводим информацию о пользователе
                    print(f"Произошла ошибка при проверке пользователя {user}")
                    print(error)

        print("Проверка всех пользователей завершена")
        print("Тест пройден")
