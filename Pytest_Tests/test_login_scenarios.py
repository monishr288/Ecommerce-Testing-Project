import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)

    inventory = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    assert inventory.is_displayed()


@pytest.mark.parametrize("username,password,message", [
    ("standard_user", "wrong123", "Username and password do not match"),
    ("", "secret_sauce", "Username is required")
])
def test_invalid_login(driver, username, password, message):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CLASS_NAME, "error-message-container")

    assert message in error.text