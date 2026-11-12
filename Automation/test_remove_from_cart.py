from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

wait.until(EC.text_to_be_present_in_element(
    (By.CLASS_NAME, "shopping_cart_badge"), "1"
))

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

wait.until(EC.url_contains("cart.html"))

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

def remove_product(driver):
    try:
        button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        button.click()
        return True
    except (StaleElementReferenceException, NoSuchElementException):
        return False

wait.until(remove_product)

wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "cart_item")))

items = driver.find_elements(By.CLASS_NAME, "cart_item")

print("Cart Items:", len(items))

assert len(items) == 0

print("Test Passed: Product removed from cart!")

driver.quit()