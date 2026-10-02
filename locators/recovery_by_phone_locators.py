from selenium.webdriver.common.by import By


class RecoveryByPhoneLocators:
    PHONE=(By.XPATH, "//input[@data-test-id='phone-input']")
    COUNTRY_LIST=(By.XPATH, "//div[@class='custom-select']")
    COUNTRY_ITEM=(By.XPATH, "//*[@class='custom-select-option-code']")
    GET_CODE=(By.XPATH, "//button[@data-test-id='phone-submit-btn']")
