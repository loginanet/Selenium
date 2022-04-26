#задача с Alerts
import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_xpath("/html/body/form/div/div/button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element(by=By.ID, value='input_value').text)
    result = str(math.log(abs(12 * math.sin(x))))
    browser.find_element(by=By.ID, value='answer').send_keys(result)
    browser.find_element_by_css_selector("button.btn").click()

except Exception as error:
    print(f'Произошла ошибка, вот ее трейсбэкЖ {error}')

finally:
    time.sleep(10)
    browser.quit()
