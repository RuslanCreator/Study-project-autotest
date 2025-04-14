from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    # Проверка, что мы находимся на странице логина, из 3-х проверок
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка на корректный url адрес
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "wrong url of login page"

    # Проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    # Проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"
        