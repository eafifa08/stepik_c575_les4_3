from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SEE_BASKET = (By.XPATH, "//span[@class='btn-group']//a")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT_IN_MESSAGES = (By.XPATH, "//div[@class='alertinner ']//strong")
    NAME_OF_PRODUCT = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")


class BasketPageLocators:
    TEXT_THAT_BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
    ITEMS_EXIST_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")

