from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SEE_BASKET = (By.XPATH, "//span[@class='btn-group']//a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")



class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT_IN_MESSAGES = (By.XPATH, "//div[@class='alertinner ']//strong")
    NAME_OF_PRODUCT = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")


class BasketPageLocators:
    TEXT_THAT_BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
    ITEMS_EXIST_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")

