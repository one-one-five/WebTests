import pytest
from selenium import webdriver
from config import BASE_URL
from pages.base_pages import BasePage
from pages.login_page import LoginPageHelper


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(browser):
    BasePage(browser).get_url(BASE_URL)
    return LoginPageHelper(browser)
