from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_xpath(".//input[contains(@class, 'first')][@required]")
        second = browser.find_element_by_xpath(".//input[contains(@class, 'second')][@required]")
        third = browser.find_element_by_xpath(".//input[contains(@class, 'third')][@required]")
        first.send_keys("Мой ответ")
        second.send_keys("Мой ответ")
        third.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name('h1')
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Text equal')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_xpath(".//input[contains(@class, 'first')][@required]")
        second = browser.find_element_by_xpath(".//input[contains(@class, 'second')][@required]")
        third = browser.find_element_by_xpath(".//input[contains(@class, 'third')][@required]")
        first.send_keys("Мой ответ")
        second.send_keys("Мой ответ")
        third.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name('h1')
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Text equal')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()