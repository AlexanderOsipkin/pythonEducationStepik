import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

download_path = file = os.path.abspath("../file_download")

options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}

options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://www.testmuai.com/"
driver.get(base_url + "selenium-playground/download-file-demo")

download_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Download File')]")
download_button.click()
print("Click download button")
time.sleep(3)

# Проверяем что директория не пустая
if os.listdir(download_path):
    print("Файл есть в директории")
else:
    print("Файла нет в директории")

print(os.listdir(download_path))

# Проверяем что скачался нужный файл и он находится в дириктории
file_name = "LambdaTest.pdf"
file_path = os.path.join(download_path, file_name)
assert os.access(file_path, os.F_OK) == True
print("Файл находится в дериктории")
time.sleep(3)

# Проверяем что файл не пуст
files = glob.glob(os.path.join(download_path, "*.*"))

for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст")

# Очистка директории
files = glob.glob(os.path.join(download_path, "*.*"))

for file in files:
    os.remove(file)
    print("Директория очищена")
