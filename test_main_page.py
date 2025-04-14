import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


# тест что, можно перейти на страницу логина с главной страницы и на ней отображаются некоторые элементы
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)    
    # открываем страницу
    page.open()                      
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()          
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# тест проверяет, что отображается элемент ссылки на страницу логина
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# тест проверяет, что можно перейти на страницу корзины товаров и отображается элемент с сообщением, что корзина пуста
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_basket_is_empty()