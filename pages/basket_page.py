from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), \
            "Basket is not empty, but should be"

    def should_be_empty_basket_line(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_LINE), \
            "Basket is empty line is not presented"
