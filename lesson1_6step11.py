# Задание: уникальность селекторов
from selenium import webdriver
import time

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//div/div/input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//div/div/input[@placeholder='Input your email']")
    input3.send_keys("aaa@mail.ru")
    input4 = browser.find_element_by_xpath("//div/div/input[@placeholder='Input your phone:']")
    input4.send_keys("phone")
    input5 = browser.find_element_by_xpath("//div/div/input[@placeholder='Input your address:']")
    input5.send_keys("address")

    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

# except Exception as error:
#     print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла