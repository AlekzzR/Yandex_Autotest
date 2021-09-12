import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(12)
    yield driver
    driver.quit()

