from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from pages.recovery_page import RecoveryPage


class LoginPageLocators:
    HEADER = (By.XPATH, "//h2[@id='login-title']")

    ENTER_TAB = (By.XPATH, "//div[@id='tabLogin']")
    LOGIN_FIELD = (By.XPATH, "//input [@id='login-phone-email']")
    PASSWORD_FIELD = (By.XPATH, "//input [@id='login-password']")
    ENTER_BUTTON = (By.XPATH, "//button[@id='login-submit-btn']")

    FORGOT = (By.XPATH, "//a[@id='forgot-password-link']")
    ERROR_TEXT = (By.XPATH, "//div[@id='login-error']")

    QR_CODE_TAB = (By.XPATH, "//div[@id='tabQr']")
    QR_CODE_IMAGE = (By.XPATH, "//div [@id='qr-placeholder']")

    HEADER_LOCKOUT = (By.XPATH, "//h2[@id='lockout-title']")
    DESCRIPTION_LOCKOUT = (By.XPATH, "//p[@id='lockout-description']")
    RECOVER_BUTTON = (By.XPATH, "//*[@id='lockout-recover-btn']")
    CANCEL_BUTTON = (By.XPATH, "//button[@id='lockout-cancel-btn']")
    REGISTER_BUTTON =  (By.XPATH, "//button[@id='lockout-register-btn']")


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.HEADER)

        self.find_element(LoginPageLocators.ENTER_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.ENTER_BUTTON)

        self.find_element(LoginPageLocators.FORGOT)

        self.find_element(LoginPageLocators.QR_CODE_TAB)

    @allure.step('нажимаем кнопку Войти')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.ENTER_BUTTON).click()

    @allure.step('вводим логин')
    def input_login(self,login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('вводим пароль')
    def input_password(self,password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('нажимаем на вкладку QR-код')
    def click_qr_tab(self):
        self.find_element(LoginPageLocators.QR_CODE_TAB).click()

    @allure.step('')
    def check_qr_code(self):
        self.find_element(LoginPageLocators.QR_CODE_IMAGE)

    @allure.step('получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVER_BUTTON).click()
        return RecoveryPage(self.driver)
