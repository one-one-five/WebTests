from core.base_tests import browser
from pages.base_pages import BasePage
from pages.login_page import LoginPageHelper


def test_empty_login_and_password(browser):
    login_page=LoginPageHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text()=='Введите телефон, email или логин и пароль.'

def test_invalid_credentials(browser):
    login_page=LoginPageHelper(browser)
    login_page.input_invalid_login()
    login_page.input_invalid_password()
    login_page.click_login()
    assert login_page.get_error_text()=='Пользователь с таким телефоном, почтой или логином не найден. Проверьте данные и попробуйте снова.'
