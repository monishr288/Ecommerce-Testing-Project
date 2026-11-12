from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("https://www.saucedemo.com/")

wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Monish")
driver.find_element(By.ID, "last-name").send_keys("R")
driver.find_element(By.ID, "postal-code").send_keys("631501")

driver.find_element(By.ID, "continue").click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout_summary_container")))

print("Checkout Information Submitted!")
print("Test Passed: Checkout details accepted!")

driver.quit()