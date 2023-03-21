import pytest
import time
import faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from .main_page import MainPage
from .login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

'''
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
   '''


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.url_logout = 'http://selenium1py.pythonanywhere.com/ru/accounts/logout/'
        self.logout_page = MainPage(browser=browser, url=self.url_logout)
        self.logout_page.open()
        self.url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        f = faker.Faker()
        email = f.email()
        pass_base = 'Netefwkrwe43'
        password = f.name() + pass_base
        password = password.replace(' ', '')

        self.product_page = ProductPage(browser=browser, url=self.url)
        self.product_page.open()
        time.sleep(5)
        self.product_page.go_to_login()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.register_new_user(email=email, password=password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_name_added()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_name_added()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_basket()
    basket_page.should_be_text_that_basket_is_empty()

