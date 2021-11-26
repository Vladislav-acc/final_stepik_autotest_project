from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest


base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.skip()
@pytest.mark.parametrize('num', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Fix later')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, num):
    full_link = f'{base_link}?promo=offer{num}'
    page = ProductPage(browser, full_link)
    page.open()
    page.should_be_put_to_basket_button()
    page.put_order_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_name_of_the_book()
    page.should_be_right_cost_of_the_book()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.put_order_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.put_order_to_basket()
    page.should_be_disappeared()
