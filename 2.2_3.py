import os

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first = browser.find_element_by_name("firstname")
    second = browser.find_element_by_name("lastname")
    third = browser.find_element_by_name("email")
    first.send_keys("Мой ответ")
    second.send_keys("Мой ответ")
    third.send_keys("Мой ответ")

    file = browser.find_element_by_name("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath(".//button[text()='Submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()