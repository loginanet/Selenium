# Задание с выпадающим списком
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    sum_element1 = int(browser.find_element_by_id("num1").text)
    sum_element2 = int(browser.find_element_by_id("num2").text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value((str(sum_element1 + sum_element2)))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла