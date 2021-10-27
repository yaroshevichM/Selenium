from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    answer = int(num1) + int(num2)
    print(answer)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(answer))  # ищем элемент с текстом "Python"
    # answer = browser.find_element_by_id("answer")
    # answer.send_keys(y)

    button = browser.find_element_by_xpath(".//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла