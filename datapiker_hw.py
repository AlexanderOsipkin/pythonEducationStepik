import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://demoqa.com/"
driver.get(base_url + "date-picker")

# Находим поле с датой
date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")

# Получаем сегодняшнюю дату
today = datetime.datetime.now()
print(today)

# Прибавляем к дате 10 дней
new_date = today + datetime.timedelta(days=10)
print("Сегодня:", today.strftime("%m/%d/%Y"))
print("Дата через 10 дней:", new_date.strftime("%m/%d/%Y"))

# Очищаем поле с датой на сайте
date_input.click()
date_input.send_keys(Keys.CONTROL + "a")
date_input.send_keys(Keys.BACKSPACE)

# Вводим новую дату в поле ввода
date_input.send_keys(new_date.strftime("%m/%d/%Y"))

# Подтверждаем ввод данных
date_input.send_keys(Keys.RETURN)
print("Новая дата успешно введена")
