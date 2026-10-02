import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    # driver.get('https://sn.rv-school.ru')
    yield driver
    driver.quit()