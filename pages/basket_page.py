from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_empty_basket(self):
        print("\nchecking basket...", end='\t')
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket should be empty, but product exist"
        print("SUCSESS")

    def should_be_empty_message(self):
        print("\nchecking empty message...", end='\t')
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Missing 'Your basket is empty' message"
        print("SUCSESS")
