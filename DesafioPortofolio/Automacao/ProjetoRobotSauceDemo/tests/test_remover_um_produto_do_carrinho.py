from selenium.webdriver.common.by import By
from conftest import driver
import pytest 

class TestRPC:
    def test_remover_um_produto_do_carrinho():
        #login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secrete_sauce")
        driver.find_element(By.ID, "login-button").click()

        #clicar no produto (mochila) no carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']")