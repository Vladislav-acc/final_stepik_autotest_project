from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_put_to_basket_button()
    page.put_order_to_basket()
    # page.solve_quiz_and_get_code()
    page.should_be_right_name_of_the_book()
    page.should_be_right_cost_of_the_book()
