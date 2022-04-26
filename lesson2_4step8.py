# Задача с ожиданием нужной цены

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    x = int(browser.find_element(by=By.ID, value='input_value').text)
    result = str(math.log(abs(12 * math.sin(x))))
    browser.find_element(by=By.ID, value='answer').send_keys(result)
    browser.find_element_by_id("solve").click()

except Exception as error:
    print(f'Произошла ошибка, вот ее трейсбэкЖ {error}')

finally:
    time.sleep(500)
    browser.quit()
