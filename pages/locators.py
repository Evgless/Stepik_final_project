from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRODUCT_NAME_CHECK = (By.CSS_SELECTOR, "div#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) strong")
    PRODUCT_PRICE_CHECK = (By.CSS_SELECTOR, "div#messages > .alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
