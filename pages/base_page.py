from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators


# Базовый класс страницы сайта, от которого наследуют другие страницы
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # Задаем неявное ожидание драйвера
        self.browser.implicitly_wait(timeout)

    # Метод проверки элемента на странице
    def is_element_present(self, type_selector, selector):
        try:
            self.browser.find_element(type_selector, selector)
        except NoSuchElementException:
            return False
        else: 
            return True
    
    # Метод открытыя окна браузера
    def open(self):
        self.browser.get(self.url)

    # Метод проверки отсутствия элемента
    def is_not_element_present(self, type_selector, selector, timeout=4):
        try:
    # Явное ожидание появления элемента за определенное время с обработкой исключения
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((type_selector, selector)))
            return False 
    # если элемент не появится за время указанное в timeout, будет выброшено исключение
        except TimeoutException:
            return True

    # Метод проверки, что элемент изчезнет через какое-то время    
    def is_disappeared(self, type_selector, selector, timeout=4):
        try:
    # Явное ожидание изчезновения элемента за определенное время с обработкой исключения
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((type_selector, selector)))
    # если элемент не появится за время указанное в timeout, будет выброшено исключение
        except TimeoutException:
            return False
        return True

    # Метод перехода на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    # Проверка наличия ссылки на страницу логина
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Метод перехода на страницу корзины товаров
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()