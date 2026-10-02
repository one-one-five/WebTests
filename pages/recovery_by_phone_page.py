from random import choice

import allure

from locators.recovery_by_phone_locators import RecoveryByPhoneLocators
from pages.base_page import BasePage


class RecoveryByPhonePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки элементов страницы'):
            self.find_element(RecoveryByPhoneLocators.PHONE)
            self.find_element(RecoveryByPhoneLocators.COUNTRY_LIST)
            self.find_element(RecoveryByPhoneLocators.GET_CODE)

    def select_random_country(self):
        self.find_element(RecoveryByPhoneLocators.COUNTRY_LIST).click()
        country_item = choice(self.find_elements(RecoveryByPhoneLocators.COUNTRY_ITEM))
        country_code = country_item.text
        country_item.click()
        return country_code

    def get_phone_field_value(self):
        return self.find_element(RecoveryByPhoneLocators.PHONE).get_attribute('value')
