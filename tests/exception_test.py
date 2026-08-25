import glob
import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

download_path = file = os.path.abspath("../file_download")

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://demoqa.com/"
driver.get(base_url + "dynamic-properties")


try:
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
except NoSuchElementException as exception:
    print("NoSuchElementException")
    time.sleep(10)
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
    print("Click visible button")

