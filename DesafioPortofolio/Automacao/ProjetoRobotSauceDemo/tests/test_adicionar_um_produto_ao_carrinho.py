import conftest
import pytest
from selenium.webdriver.common.by import By




class CT01:
    def test_adicionar_um_produto_carrinho(self):
        
        #login
        campo_login = browser.find_element(By.ID,"user-name").send_keys("standard_user")
        campo_senha = browser.find_element(By.ID, "password").send_keys("secret_sauce")
        botao_login = browser.find_element(By.ID, "login-button").click()

        #adicionar um produto ao carrinho
        driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[@class='btn btn_primary btn_small btn_inventory']").click()

        #verificar se o produto foi adicionado ao carrinho
        driver.find_element(By.XPATH, " //*[@class='shopping_cart_link'] ").click()
        assert driver.find_element(By.XPATH, " //*[@class='inventory_item_name' and text()='Sauce Labs Backpack'] ").is_displayed()
        