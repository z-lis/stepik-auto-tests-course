from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    value_x = browser.find_element_by_id("input_value")
    x = value_x.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально скопировать результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
