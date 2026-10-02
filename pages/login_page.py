from locators.login_locators import LoginLocators
from pages.base_page import BasePage
import allure
from pages.recovery_page import RecoveryPage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.attach_screenshot()
        self.find_element(LoginLocators.HEADER)

        self.find_element(LoginLocators.ENTER_TAB)
        self.find_element(LoginLocators.LOGIN_FIELD)
        self.find_element(LoginLocators.PASSWORD_FIELD)
        self.find_element(LoginLocators.ENTER_BUTTON)

        self.find_element(LoginLocators.FORGOT)

        self.find_element(LoginLocators.QR_CODE_TAB)

    @allure.step('нажимаем кнопку Войти')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginLocators.ENTER_BUTTON).click()

    @allure.step('вводим логин')
    def input_login(self,login):
        self.find_element(LoginLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('вводим пароль')
    def input_password(self,password):
        self.find_element(LoginLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('нажимаем на вкладку QR-код')
    def click_qr_tab(self):
        self.find_element(LoginLocators.QR_CODE_TAB).click()

    @allure.step('проверяем отображение QR-кода»')
    def check_qr_code(self):
        self.find_element(LoginLocators.QR_CODE_IMAGE)

    @allure.step('получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginLocators.ERROR_TEXT).text

    @allure.step('переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginLocators.RECOVER_BUTTON).click()
        return RecoveryPage(self.driver)
