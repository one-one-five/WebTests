from pages.base_pages import BasePage
from selenium.webdriver.common.by import By
import allure


class RecoveryPageLocators:
    HEADERS_RECOVERY = (By.XPATH, "//h1[@id='recovery-title']")
    PHONE = (By.XPATH, "//a[@id='recovery-phone-btn']")
    E_MAIL = (By.XPATH, "//a[@id='recovery-email-btn']")
    QR = (By.XPATH, "//div[@id='qr-image']")
    QR_INFO = (By.XPATH, "//div[@id='qr-info']")
    SUPPORT_BUTTON = (By.XPATH, "//button[@id='support-contact-btn']")


class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(RecoveryPageLocators.PHONE)
        self.find_element(RecoveryPageLocators.E_MAIL)
        self.find_element(RecoveryPageLocators.QR)
        self.find_element(RecoveryPageLocators.QR_INFO)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)
