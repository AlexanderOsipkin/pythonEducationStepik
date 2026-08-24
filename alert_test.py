import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://the-internet.herokuapp.com/"
driver.get(base_url + "javascript_alerts")

# Есть какая-то 1 кнопка, например ОК
js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
js_alert.click()
print("Click alert button")

print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()

time.sleep(3)

# Есть кнопка и ОК и ОТМЕНА
js_confirmon = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
js_confirmon.click()
print("Click confirmon button")

print(driver.switch_to.alert.text)
# driver.switch_to.alert.accept()  # подтвердить
driver.switch_to.alert.dismiss()  # отклонить
