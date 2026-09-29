from pages.base_pages import BasePage
from selenium.webdriver.common.by import By


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


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.HEADER)

        self.find_element(LoginPageLocators.ENTER_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.ENTER_BUTTON)

        self.find_element(LoginPageLocators.FORGOT)

        self.find_element(LoginPageLocators.QR_CODE_TAB)

    def click_login(self):
        self.find_element(LoginPageLocators.ENTER_BUTTON).click()

    def click_qr_tab(self):
        self.find_element(LoginPageLocators.QR_CODE_TAB).click()

    def check_qr_code(self):
        self.find_element(LoginPageLocators.QR_CODE_IMAGE)

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text
