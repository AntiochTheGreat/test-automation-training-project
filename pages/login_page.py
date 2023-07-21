from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Invalid URL'

    def should_be_login_form(self):
        login_form_element = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form_element.is_displayed(), 'Login form not found'

    def should_be_register_form(self):
        register_form_element = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form_element.is_displayed(), 'Register form not found'

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        input_password.send_keys(password)
        input_repeat_password = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_FIELD)
        input_repeat_password.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button_registration.click()

