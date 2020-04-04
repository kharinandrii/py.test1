from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD_LOCATOR = (By.XPATH, "//input[@id='LoginForm_username']")
    PASS_FIELD_LOCATOR = (By.XPATH, "//input[@id='LoginForm_password']")
    AUTH_BUTTON = (By.XPATH, "//button[@id='Authorization']")