from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://demoqa.com/"
driver.get(base_url + "dynamic-properties")
# driver.implicitly_wait(10)  # ожидает каждый элемент, то время, которое указано
#
# print("Start test")
# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# visible_button.click()
# print("Finish test")

print("Start test")
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                             "//button[@id='visibleAfter']")))  # задаем время в течении которого тест будет ждать этот элемент, что бы он стал кликабельным (мы могли на него нажать)
visible_button.click()
print("Finish test")
