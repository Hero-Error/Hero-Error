from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Credentials
email = "afk@Bot.com"
password = "Error-0.1"

# Set up Chrome WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    # Go to login page
    driver.get("https://cm8lcm-3001.csb.app/login")

    # Optional preview button
    try:
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Yes, proceed to preview")]')))
        button.click()
        print("Clicked preview button.")
    except:
        print("Preview button not found or skipped.")

    # Wait for at least 2 input fields to be present
    input_fields = wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "input")) >= 2)
    inputs = driver.find_elements(By.TAG_NAME, "input")

    # Fill in email and password
    inputs[0].send_keys(email)
    inputs[1].send_keys(password)
    print("Filled email and password.")

    # Click the "Sign in" button
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign in")]')))
    sign_in_button.click()
    print("Clicked Sign in.")

    # Wait for AFK page to load
    time.sleep(5)
    driver.get("https://cm8lcm-3001.csb.app/afk")
    print("AFK page loaded.")

    # Stay AFK
    for i in range(120):
        print(f"AFK minute {i + 1}")
        time.sleep(60)

except Exception as e:
    print(f"Error: {e}")

finally:
    print("Ending session.")
    driver.quit()
