from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
)

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

print("Cart Count:", cart.text)

assert cart.text == "1"

print("Test Passed: Product added to cart!")

driver.quit()