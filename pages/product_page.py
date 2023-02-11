from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_add_cart_button(self):
        add_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_cart_button.click()

    def collect_product_name_and_price(self):
        print("\ncollecting data...", end='\t')
        global product_name
        global product_price
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # print('\nproduct name is "', product_name, '"')
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # print('\nproduct price is "', product_price, '"')
        print("Sucsess")

    def should_match_product_name(self):
        print("\nchecking product name...", end='\t')
        product_name_check = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CHECK).text
        assert product_name == product_name_check, "Product name not match"
        print("Sucsess")
        # print(product_name_check, product_name)

    def should_match_product_price(self):
        print("\nchecking product price...", end='\t')
        product_price_check = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CHECK).text
        assert product_price == product_price_check, "Product price not match"
        print("Sucsess")
        # print(product_price_check, product_price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"
