from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def test_add_seasonal_category(driver, email, password, month_name):
    # Step 1: Login
    driver.get("http://127.0.0.1:8000/login/")  # Change to your actual login URL

    try:
        # Wait for the email input and enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)
        time.sleep(1)

        # Wait for password input and enter password
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(password)
        time.sleep(1)

        # Submit login form
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)
        print("Login successful!")

        # Step 2: Navigate to the seasonal category form
        driver.get("http://127.0.0.1:8000/seasonal_category/")  # Update with actual URL

        # Wait for the form elements to load
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "month_name"))
        )

        # Step 3: Fill the form
        month_input = driver.find_element(By.ID, "month_name")
        month_input.send_keys(month_name)  # Enter month name
        time.sleep(1)
        print(f"Entered month name: {month_name}")

        # Step 4: Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(2)

        # Step 5: Verify success message
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
        )
        print(f"Seasonal category '{month_name}' added successfully.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

# Initialize WebDriver (Use Edge, Chrome, or Firefox)
driver = webdriver.Edge()  # Change to Chrome() if needed

# Run the test
test_add_seasonal_category(driver, "education@gmail.com", "Education@123", "August")
