import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://www.testmuai.com/"
driver.get(base_url + "selenium-playground/simple-form-demo")
time.sleep(2)

massage = "Hello World"
input_field = driver.find_element(By.XPATH, "//input[@id='user-message']")
input_field.send_keys(massage)

show_input = driver.find_element(By.XPATH, "//button[@id='showInput']")
show_input.click()

massage_field = driver.find_element(By.XPATH, "//p[@id='message']")
value_massage_field = massage_field.text
print(value_massage_field)

assert value_massage_field == massage
print("all good")

num_1 = 1
input_first_value_field = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_first_value_field.send_keys(num_1)
print(input_first_value_field)

num_2 = 2
input_second_value_field = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_second_value_field.send_keys(num_2)

get_sum_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Get Sum')]")
get_sum_button.click()

sum_massage_field = driver.find_element(By.XPATH, "//p[@id='addmessage']")
value_sum_massage_field = sum_massage_field.text

sum_result = num_1 + num_2
assert value_sum_massage_field == str(sum_result)
print("all good 2")