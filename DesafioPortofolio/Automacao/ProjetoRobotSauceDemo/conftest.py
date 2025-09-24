import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    #setup
    #global driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)   
    #driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver

    driver.quit()