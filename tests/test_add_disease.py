from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def test_add_disease(driver, email, password, title, image_path, description, tips_to_control):
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

        # Step 2: Navigate to the 'Add Disease' form
        driver.get("http://127.0.0.1:8000/add_disease/")  # Update with actual URL

        # Wait for form elements to load
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "title"))
        )

        # Step 3: Fill the form
        title_input = driver.find_element(By.NAME, "title")
        title_input.send_keys(title)
        time.sleep(1)
        
        image_input = driver.find_element(By.NAME, "image")
        image_input.send_keys(image_path)  # Uploading image
        time.sleep(1)

        description_input = driver.find_element(By.NAME, "description")
        description_input.send_keys(description)
        time.sleep(1)

        tips_input = driver.find_element(By.NAME, "tips_to_control")
        tips_input.send_keys(tips_to_control)
        time.sleep(1)

        # Step 4: Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(2)

        # Step 5: Verify success message
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
        )
        print(f"Disease '{title}' added successfully.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

# Initialize WebDriver (Use Edge, Chrome, or Firefox)
driver = webdriver.Edge()  # Change to Chrome() if needed

# Run the test
test_add_disease(driver, "education@gmail.com", "Education@123", "Leaf Blight", "myproject/myapp/static/img/crp.jpeg"
, "A common fungal disease.", "Use fungicide and proper irrigation.")
