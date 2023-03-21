from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_EXIST_IN_BASKET), "Items exist in basket"

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_THAT_BASKET_IS_EMPTY), 'No text, that basket is empty'
