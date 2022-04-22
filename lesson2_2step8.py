#задача с загрузкой файла
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys("Имя")
    browser.find_element_by_name("lastname").send_keys("Фамилия")
    browser.find_element_by_name("email").send_keys("емейл")
    current_dir = os.path.abspath(os.path.dirname("D:\ "))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_name("file").send_keys(file_path)
    browser.find_element_by_css_selector("button.btn").click()

except Exception as error:
    print(f'Произошла ошибка, вот ее трейсбэк: {error}')

finally:
    time.sleep(10)
    browser.quit()
