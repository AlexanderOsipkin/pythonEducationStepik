from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

base_url = "https://html5css.dev/howto/howto_js_rangeslider.php"
driver.get(base_url)

action = ActionChains(driver)

# Взаимодействие с ползунком громкости и тд
range_input = driver.find_element(By.XPATH, "//input[@id='id1']")
action.click_and_hold(range_input).move_by_offset(200,
                                                  0).release().perform()  # release - отпускаем мыш, perfom - сохраняем
