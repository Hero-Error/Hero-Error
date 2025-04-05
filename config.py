from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Credentials
email = "afk@Bot.com"
password = "Error-0.1"

# Set up Chrome WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Go to login page
    driver.get("https://cm8lcm-3001.csb.app/login")

    # Optional: Click "Yes, proceed to preview" button
    try:
        button = driver.find_element(By.XPATH, '//button[contains(text(), "Yes, proceed to preview")]')
        button.click()
        print("Clicked preview button.")
    except Exception as e:
        print("Preview button not found or already skipped.")

    time.sleep(2)

    # Find all input fields
    input_fields = driver.find_elements(By.TAG_NAME, "input")

    # Fill in email and password
    if len(input_fields) >= 2:
        input_fields[0].send_keys(email)
        input_fields[1].send_keys(password)
        print("Filled in email and password.")
    else:
        raise Exception("Unable to find email and password input fields.")

    # Click the "Sign in" button
    sign_in_button = driver.find_element(By.XPATH, '//button[contains(text(), "Sign in")]')
    sign_in_button.click()
    print("Clicked Sign in button.")

    time.sleep(5)

    # Go to AFK page
    driver.get("https://cm8lcm-3001.csb.app/afk")
    print("Navigated to AFK page.")

    # Stay AFK
    for i in range(120):
        print(f"AFK for minute {i + 1}")
        time.sleep(60)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Ending session.")
    driver.quit()
