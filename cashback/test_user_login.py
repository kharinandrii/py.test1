from pages.login_page import LoginPage
import pytest

def test_login_admin(browser):
    link = "http://ag.t.ukrtech.info/site/login/index"
    login_page = LoginPage(browser, link)
    browser.get(link)
    login_page.get_login_field("admin")
    login_page.get_pass_field("123456q")
    login_page.click_auth_button()

