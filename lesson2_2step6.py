from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(by=By.ID, value='input_value').text)
    result = str(math.log(abs(12*math.sin(x))))
    browser.find_element(by=By.ID, value='answer').send_keys(result)
    browser.find_element(by=By.ID, value='robotCheckbox').click()
    option = browser.find_element(by=By.ID, value='robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option)
    option.click()
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот ее трейсбэк: {error}')

finally:
    # успеваем скопировать за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла