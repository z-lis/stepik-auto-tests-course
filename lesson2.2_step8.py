from selenium import webdriver
import time
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    name.send_keys("Жубан")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Ибрагимович")

    email = browser.find_element_by_name("email")
    email.send_keys("juban@jija.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input_file = browser.find_element_by_id("file")
    input_file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально скопировать результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
