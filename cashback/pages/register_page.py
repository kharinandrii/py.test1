from .base_page import BasePage
from .locators import RegisterPageLocators

class RegisterPage(BasePage):

    def fill_user_login(self, user_login):
        login_field = self.browser.find_element(*RegisterPageLocators.USER_LOGIN_LOCATOR)
        login_field.send_keys(user_login)