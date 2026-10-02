import allure

from pages.recovery_page import RecoveryPage

LOGIN_TEXT = 'login'
PASSWORD_TEXT = '1'


@allure.suite('проверка восстановления пользователя')
@allure.title('проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_many_fails(login_page):
    login_page.input_login(LOGIN_TEXT)

    for _ in range(3):
        login_page.input_password(PASSWORD_TEXT)
        login_page.click_login()

    login_page.click_recovery()

    # RecoveryPageHelper(login_page)
