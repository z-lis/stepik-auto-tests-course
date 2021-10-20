from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id("num1")
    num1 = number1.text
    number2 = browser.find_element_by_id("num2")
    num2 = number2.text

    x = (int(num1) + int(num2))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(x))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально скопировать результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()