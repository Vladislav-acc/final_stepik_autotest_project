from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_SUMMARY = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY_LINE = (By.CSS_SELECTOR, "#content_inner p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD_IN_REGISTRATION_FORM = (
        By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_IN_REGISTRATION_FORM = (
        By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_IN_REGISTRATION_FORM = (
        By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (
        By.CSS_SELECTOR, "#register_form button[name='registration_submit']")


class ProductPageLocators():
    PUT_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BOOK_COST = (By.CSS_SELECTOR, "div.product_main p.price_color")
    BOOK_NAME_IN_ALERT = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    BOOK_COST_IN_ALERT = (By.XPATH, "//div[@id='messages']/div[3]//strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")
