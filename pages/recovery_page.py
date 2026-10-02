from locators.recovery_locators import RecoveryLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.attach_screenshot()
        self.find_element(RecoveryLocators.PHONE)
        self.find_element(RecoveryLocators.E_MAIL)
        self.find_element(RecoveryLocators.QR)
        self.find_element(RecoveryLocators.QR_INFO)
        self.find_element(RecoveryLocators.SUPPORT_BUTTON)
