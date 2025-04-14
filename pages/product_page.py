from .base_page import BasePage
from pages.locators import ProductPageLocators

from selenium.common.exceptions import NoAlertPresentException 
import math
import time


class ProductPage(BasePage):
    # Метод получения названия товара со страницы
    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    # Метод получения цены товара со страницы
    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    
    # Проверка добавления товара в корзину из 2-х проверок
    def should_be_added_poduct_to_basket(self):
        self.should_be_success_message()
        self.should_be_changed_basket_total_price()

    # Проверка соответствия названия товара на странице товара и в сообщение о добавлении в корзину      
    def should_be_success_message(self):
        assert self.product_name() == self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_PRODUCT).text, "wrong success message about added"
    
    # Проверка соответствия цены товара на странице товара и в сообщение о изменении суммы корзины
    def should_be_changed_basket_total_price(self):
        assert self.product_price() == self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text, "wrong basket total"

    # Метод добавления товара в корзину
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        # Метод применения Javascript для прокрутки страницы вниз, пока не станет видна кнопка добавления товара
        self.browser.execute_script("arguments[0].scrollIntoView(true);", add_button)
        add_button.click()

    # Проверка отсутствия сообщения о добавлении товара в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_PRODUCT), \
        "Success message is presented, but should not be" 

    # Проверка, что сообщение о добавление товара изчезнет через какое-то время
    def should_disappeare_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_PRODUCT), \
        "Success message isn't disappeared"

    # Метод для прохождения проверки в alert для тестов с промокодами
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(3)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")