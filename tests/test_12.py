import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://demoqa.com/"
driver.get(base_url + "date-picker")

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.click()
# new_date.send_keys(Keys.CONTROL + "a")
# new_date.send_keys(Keys.BACKSPACE)
#
# time.sleep(3)
# new_date.send_keys("08/27/2026")
#
# time.sleep(3)
# new_date.send_keys(Keys.RETURN)
now_date = datetime.datetime.now().strftime("%d")
print(now_date)
date = int(now_date)
locator = "//div[@aria-label='Choose Friday, August " + str(date) + "st, 2026']"
print(locator)

new_date.click()
time.sleep(3)
new_date_27 = driver.find_element(By.XPATH, locator)
# new_date_27 = driver.find_element(By.XPATH,
#                                   "//div[@aria-label='Choose Thursday, August 27th, 2026']")
# //div[contains(@class,'react-datepicker__day react-datepicker__day--027')]
new_date_27.click()

