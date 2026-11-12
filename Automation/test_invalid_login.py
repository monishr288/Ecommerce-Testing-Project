
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("wrong_password")

driver.find_element(By.ID, "login-button").click()

error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
)

print("Actual Result:", error.text)

assert "Username and password do not match" in error.text

print("Test Passed: Invalid login rejected!")

driver.quit()
