import os

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://practice-automation.com/"
driver.get(base_url + "file-upload")

file = os.path.abspath("../file_upload/file1.jpg")

chose_file_button = driver.find_element(By.XPATH, "//input[@id='file-upload']")
chose_file_button.send_keys(file)
print("Click to the chose file button")

upload_button = driver.find_element(By.XPATH, "//input[@id='upload-btn']")
upload_button.click()
print("Click to the upload button")

