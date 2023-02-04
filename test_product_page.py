from .pages.product_page import ProductPage

def test_guest_can_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.collect_product_name_and_price()
    page.press_add_cart_button()
    page.solve_quiz_and_get_code()
    page.should_match_product_name()
    page.should_match_product_price()