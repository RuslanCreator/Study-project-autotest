import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


# тест проверяет, что можно добавить товар в корзину и не появится сообщение об успешном добавлении
@pytest.mark.skip
# пропускаем падающий тест
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

# тест проверяет, что сообщение о добавление товара в корзину пропадет через какое-то время после открытия страницы товара
@pytest.mark.skip
# пропускаем падающий тест
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappeare_success_message()

# класс тестов взаимодействия с ссылкой логина на странице продукта
class TestGuestInteractLoginLink():

# тест проверяет, что на странице товара отображается элемент ссылки на страницу логина 
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

# тест проверяет, что на странице товара можно перейти на страницу логина по ссылки и проверяет наличие элементов на ней
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()          
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


# класс тестов взаимодействия со страницей корзины товаров на странице продукта
class TestGeustAddToBasketFromProductPage():

# тест проверяет, что можно добавить товар с различных страниц(параметр - ключ ссылки) товара и потом проходит проверку в окне alert
    @pytest.mark.parametrize('promo', ["offer0",
                                    "offer1",
                                    "offer2"
    ])
    def test_guest_can_add_product_to_basket(self, browser, promo):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_added_poduct_to_basket()

# тест проверяет, что нет сообщения о добавление товара в корзину при откртии страницы товара
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

# тест проверяет, что на странице продукта можно перейти на страницу корзины по ссылке, и что корзина пуста
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser, browser.current_url)
        page.should_basket_is_empty()