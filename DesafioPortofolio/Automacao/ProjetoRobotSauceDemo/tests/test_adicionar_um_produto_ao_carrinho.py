from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest





@pytest.mark.usefixtures("setup_teardown")
class TestAdicionarProdutoCarrinho:
    def test_adicionar_um_produto_carrinho(self,setup_teardown):
        driver = setup_teardown
        
        #login
        campo_login = driver.find_element(By.ID,"user-name").send_keys("standard_user")
        campo_senha = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        botao_login = driver.find_element(By.ID, "login-button").click()

       


        #adicionar um produto no carrinho
        driver.find_element(By.XPATH, " //*[@class='inventory_item_name ' and text()='Sauce Labs Backpack'] ").click()
        driver.find_element(By.XPATH, "//*[@class='btn btn_primary btn_small btn_inventory']").click()

        #verificar se o produto foi adicionado ao carrinho
        driver.find_element(By.XPATH, " //*[@class='shopping_cart_link'] ").click()
        assert driver.find_element(By.XPATH, " //*[@class='inventory_item_name' and text()='Sauce Labs Backpack'] ").is_displayed()