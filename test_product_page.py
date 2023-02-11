import pytest
from .pages.product_page import ProductPage

@pytest.mark.skip
@pytest.mark.parametrize('offer_number', [*range(7),
                                          pytest.param("7", marks=pytest.mark.skip),
                                          *range(8, 10)])
def test_guest_can_add_to_cart(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser, link)
    page.open()
    page.collect_product_name_and_price()
    page.press_add_cart_button()
    page.solve_quiz_and_get_code()
    page.should_match_product_name()
    page.should_match_product_price()

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_add_cart_button()
    # page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    pass
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    pass

@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_add_cart_button()
    # page.solve_quiz_and_get_code()
    page.should_be_dissappeared()
    pass

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

