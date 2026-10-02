import pytest
from selenium import webdriver

from config import BASE_URL
from pages.base_page import BasePage
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    BasePage(driver).get_url(BASE_URL)
    return LoginPage(driver)
