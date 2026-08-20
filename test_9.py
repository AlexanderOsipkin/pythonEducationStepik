from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://demoqa.com/"
driver.get(base_url + "checkbox")

checkbox = driver.find_element(By.XPATH, "//span[@role='checkbox']")
checkbox.click()

checkboxTree = driver.find_element(By.XPATH,
                                   "//*[@id='root']/div/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/span[2]")
checkboxTree.click()
