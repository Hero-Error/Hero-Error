from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Open the page
driver.get("https://2pn7dw-8080.csb.app/auth/login")  # Replace with your actual URL

# Number of times to reload the page
reload_count = 100000

for _ in range(reload_count):
    try:
        # Try to find and click the button
        button = driver.find_element(By.XPATH, '//button[contains(text(), "Yes, proceed to preview")]')
        button.click()
        print("Button clicked successfully!")
    except Exception as e:
        print(f"Button not found, skipping click. Error: {e}")

    # Wait for 3 minutes before refreshing
    time.sleep(60)

    # Refresh the webpage
    driver.refresh()
    print("Webpage reloaded!")

# Quit the browser after 3 reloads
print("Task completed. Closing the browser.")
driver.quit()
