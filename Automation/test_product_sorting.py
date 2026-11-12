from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")

Select(dropdown).select_by_value("lohi")

prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

price_list = [float(price.text.replace("$", "")) for price in prices]

print("Sorted Prices:", price_list)

assert price_list == sorted(price_list)

print("Test Passed: Products sorted by low to high price!")

driver.quit()