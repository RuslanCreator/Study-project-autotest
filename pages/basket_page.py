from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверка корзины на отсутствие товаров, включающая 2 проверки
    def should_basket_is_empty(self):
        self.should_be_message_empty_basket()
        self.should_not_be_product_in_basket()

    # Проверка наличия элемента, содержащего сообщение об отсутствии товара в корзине
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
        "Message 'basket empty' is not present"

    # Проверка отсутствия элемента, содержащего информацию о товаре
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
        "There's product in basket"