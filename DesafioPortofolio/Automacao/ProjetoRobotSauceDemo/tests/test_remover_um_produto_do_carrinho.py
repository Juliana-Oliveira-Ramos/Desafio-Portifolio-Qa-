from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest 

@pytest.mark.usefixtures("setup_teardown")
class TestRPC:
    def test_remover_um_produto_do_carrinho(self,setup_teardown):
        driver = setup_teardown
        #login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
         
        #adicionar um produto no carrinho
        driver.find_element(By.XPATH, " //*[@class='inventory_item_name ' and text()='Sauce Labs Backpack'] ").click()
        driver.find_element(By.XPATH, "//*[@class='btn btn_primary btn_small btn_inventory']").click()

        #verificar se o produto foi adicionado ao carrinho
        driver.find_element(By.XPATH, " //*[@class='shopping_cart_link'] ").click()
        assert driver.find_element(By.XPATH, " //*[@class='inventory_item_name' and text()='Sauce Labs Backpack'] ").is_displayed()

        #clicar no botao remover 
        