from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_put_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.PUT_TO_BASKET),\
            'Put to basket button is not presented'

    def put_order_to_basket(self):
        put_to_basket_button = self.browser.find_element(
            *ProductPageLocators.PUT_TO_BASKET)
        put_to_basket_button.click()

    def should_be_right_name_of_the_book(self):
        assert self.find_text(
            *ProductPageLocators.BOOK_NAME_IN_ALERT) == self.find_text(*ProductPageLocators.BOOK_NAME),\
            "Book name in basket is not the same"

    def should_be_right_cost_of_the_book(self):
        assert self.find_text(
            *ProductPageLocators.BOOK_COST_IN_ALERT) == self.find_text(*ProductPageLocators.BOOK_COST),\
            "Book cost in basket is not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"
