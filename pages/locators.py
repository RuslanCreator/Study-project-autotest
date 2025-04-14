from selenium.webdriver.common.by import By

# класс с локаторами элементов на всех страницах
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a")

class MainPageLocators():
    pass

# класс с локаторами элементов на странице логина
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")  # #login_form.well correct selector
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    MESSAGE_ADD_PRODUCT = (By.CSS_SELECTOR, "div.page_inner div.alert-success:nth-child(1) div.alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info div.alertinner p:nth-child(1) strong")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner article.product_page")