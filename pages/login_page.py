from pages.base_pages import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_TAB = (By.XPATH, "//a[@title='Вход']")

    QR_CODE_TAB = (By.XPATH, "//a[@title='QR-код']")
    QR_CODE_IMAGE = (By.XPATH, "//img[@class='qr_code_image']")

    LOGIN_FIELD = (By.XPATH, "//input[@data-test-id='login-input']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-test-id='password-input']")
    SHOW_PASSWORD = (By.XPATH, "//button[normalize-space()='Показать пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[@data-test-id='enter-action']")
    QR_ENTER_BUTTON = (By.XPATH, "//button[normalize-space()='Войти по QR-коду']")
    FORGOT = (By.XPATH, "//button[@data-test-id='forgot-password-link']")
    REGISTRATION = (By.XPATH, "//button[@data-test-id='registration-action']")
    VK = (By.XPATH, "//a[@title='Войти через VK ID']")
    MAIL = (By.XPATH, "//a[@title='Войти через Почту']")
    YANDEX = (By.XPATH, "//a[@title='Войти через Яндекс']")


class LoginPageHelper(BasePage):
    pass
