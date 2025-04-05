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

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://cm8lcm-3001.csb.app/login")

    # Optional preview gate
    try:
        preview_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Yes, proceed to preview")]')))
        preview_button.click()
        print("Clicked preview button.")
    except:
        print("Preview button not found or skipped.")

    # Wait for email field and fill it
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    print("Email and password entered.")

    # Click "Sign in"
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign in")]'))).click()
    print("Clicked Sign in.")

    # Wait for login to complete
    time.sleep(5)

    # Go to AFK page
    driver.get("https://cm8lcm-3001.csb.app/afk")
    print("AFK page loaded.")

    # Stay AFK
    for i in range(120):
        print(f"AFK minute {i + 1}")
        time.sleep(60)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    print("Ending session.")
    driver.quit()
