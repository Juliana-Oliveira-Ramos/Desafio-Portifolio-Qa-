import time
from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()


browser.get("https://www.saucedemo.com/")
time.sleep(5)

def realizar_login():
    campo_login = browser.find_element(By.ID,"user-name").send_keys("standard_user")
    campo_senha = browser.find_element(By.ID, "password").send_keys("secret_sauce")
    botao_login = browser.find_element(By.ID, "login-button").click()



realizar_login()