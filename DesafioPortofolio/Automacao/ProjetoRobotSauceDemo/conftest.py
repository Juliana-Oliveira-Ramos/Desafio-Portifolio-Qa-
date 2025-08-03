import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    #setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/inventory.html")
    yield

    driver.quit()