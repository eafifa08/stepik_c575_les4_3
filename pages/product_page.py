from base_page import BasePage
from selenium.webdriver.common.by import By
from locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket link is not presented"

    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_link.click()

    def should_be_name_added(self):
        assert self.is_element_present(*ProductPageLocators.NAME_OF_PRODUCT_IN_MESSAGES), 'No name of product in messages'

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.NAME_OF_PRODUCT), 'No name of product'

    def should_be_equal_names(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text == \
               self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_MESSAGES).text,\
            'No name of product in messages'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_OF_PRODUCT_IN_MESSAGES), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_OF_PRODUCT_IN_MESSAGES), \
            "Success message is presented, but should be disappear"
