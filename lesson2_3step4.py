#задача с Alerts
import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("button.btn").click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element(by=By.ID, value='input_value').text)
    result = str(math.log(abs(12 * math.sin(x))))
    browser.find_element(by=By.ID, value='answer').send_keys(result)
    browser.find_element_by_css_selector("button.btn").click()

except Exception as error:
    print(f'Произошла ошибка, вот ее трейсбэкЖ {error}')

finally:
    time.sleep(10)
    browser.quit()
