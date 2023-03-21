from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Not correct url address for login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login()
        el_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        el_email.click()
        el_email.send_keys(email)
        el_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        el_password1.click()
        el_password1.send_keys(password)
        el_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        el_password2.click()
        el_password2.send_keys(password)
        el_register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        el_register_btn.click()

