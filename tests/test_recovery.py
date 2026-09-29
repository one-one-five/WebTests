import allure
from pages.base_pages import BasePage
from core.base_tests import browser
from pages.login_page import LoginPageHelper
from pages.recovery_page import RecoveryPageHelper



LOGIN_TEXT='login'
PASSWORD_TEXT='1'

@allure.suite('проверка восстановления пользователя')
@allure.title('проверка перехода к восстановлению после нескольких неудачный попыток авторизации')
def test_go_to_recovery_many_fails(browser):
    login_page = LoginPageHelper(browser)
    login_page.input_login(LOGIN_TEXT)

    for i in range(3):
        login_page.input_password(PASSWORD_TEXT)
        login_page.click_login()

    login_page.click_recovery
    login_page.attach_screenshot()

    recovery_page=RecoveryPageHelper(browser)