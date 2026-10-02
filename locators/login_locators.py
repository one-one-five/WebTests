from selenium.webdriver.common.by import By


class LoginLocators:
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
