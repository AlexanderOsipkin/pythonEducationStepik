import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://www.lambdatest.com/"
driver.get(base_url + "selenium-playground/iframe-demo")
time.sleep(2)

iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)  # Обращаемся к нашему  iframe для получения корректного значения для инпута

iframe_message = "Hello World"

iframe_input = driver.find_element(By.XPATH, "//div[@id='__next']/div/div/div[2]")
iframe_input.click()

iframe_input.send_keys(Keys.CONTROL + "a")
iframe_input.send_keys(Keys.BACKSPACE)

iframe_input.send_keys(iframe_message)
value_iframe_input = iframe_input.text
print(value_iframe_input)

iframe_input.send_keys(Keys.CONTROL + "a")

# выделяем жирным
iframe_edition_panel_bold = driver.find_element(By.XPATH, "//button[@title='Bold']")
iframe_edition_panel_bold.click()

bold_value = driver.find_element(By.XPATH, "//div[@id='__next']/div/div/div[2]/b")
bold_text = bold_value.text  # переводим в текст для ассерта

assert value_iframe_input == bold_text
print("Редактирование успешно")

# выделяем курсивом
iframe_input.send_keys(Keys.CONTROL + "a")
iframe_edition_panel_italic = driver.find_element(By.XPATH, "//button[@title='Italic']")
iframe_edition_panel_italic.click()

italic_value = driver.find_element(By.XPATH, "//div[@id='__next']/div/div/div[2]/b/i")
italic_text = italic_value.text  # переводим в текст для ассерта

assert value_iframe_input == italic_text == bold_text
print("Текст успешно выделен жирным и курсивом")
