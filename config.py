from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Credentials
email = "afk@Bot.com"
password = "Error-0.1"

# Set up the Chrome WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Go to login page
    driver.get("https://cm8lcm-3001.csb.app/login")

    # Click "Yes, proceed to preview" if the button exists
    try:
        button = driver.find_element(By.XPATH, '//button[contains(text(), "Yes, proceed to preview")]')
        button.click()
        print("Clicked preview button.")
    except Exception as e:
        print("Preview button not found or already skipped.")

    # Wait for login form to load
    time.sleep(2)

    # Fill email and password
    driver.find_element(By.NAME, "Username").send_keys(email)
    driver.find_element(By.NAME, "Password").send_keys(password)

    # Submit the form
    driver.find_element(By.XPATH, '//button[contains(text(), "Login")]').click()
    print("Login form submitted.")

    # Wait for login to complete
    time.sleep(5)

    # Go to AFK page
    driver.get("https://cm8lcm-3001.csb.app/afk")
    print("Navigated to AFK page.")

    # Stay AFK
    afk_duration_minutes = 120
    for i in range(afk_duration_minutes):
        print(f"AFK for minute {i + 1}")
        time.sleep(60)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Ending session.")
    driver.quit()
