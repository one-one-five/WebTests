from selenium.webdriver.common.by import By


class RecoveryLocators:
    HEADERS_RECOVERY = (By.XPATH, "//h1[@id='recovery-title']")
    PHONE = (By.XPATH, "//*[@id='recovery-phone-btn']")
    E_MAIL = (By.XPATH, "//*[@id='recovery-email-btn']")
    QR = (By.XPATH, "//div[@id='qr-image']")
    QR_INFO = (By.XPATH, "//div[@id='qr-info']")
    SUPPORT_BUTTON = (By.XPATH, "//button[@id='support-contact-btn']")
