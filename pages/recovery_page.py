import allure

from locators.recovery_locators import RecoveryLocators
from pages.base_page import BasePage
from pages.recovery_by_phone_page import RecoveryByPhonePage

#from pages.recovery_by_phone_page import RecoveryByEmailPage


class RecoveryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки элементов страницы'):
            self.attach_screenshot()
            self.find_element(RecoveryLocators.PHONE)
            self.find_element(RecoveryLocators.E_MAIL)
            self.find_element(RecoveryLocators.QR)
            self.find_element(RecoveryLocators.QR_INFO)
            self.find_element(RecoveryLocators.SUPPORT_BUTTON)

    @allure.step('кликаем по кнопке восстановить с помощью телефона')
    def click_recovery_by_phone(self):
        self.attach_screenshot()
        self.find_element(RecoveryLocators.PHONE).click()
        return RecoveryByPhonePage(self.driver)

    # @allure.step('кликаем по кнопке восстановить с помощью e-mail')
    # def click_recovery_by_email(self):
    #     self.attach_screenshot()
    #     self.find_element(RecoveryLocators.E_MAIL).click()
    #     return RecoveryByEmailPage(self.driver)
