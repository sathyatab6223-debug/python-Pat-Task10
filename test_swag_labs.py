import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """
    Initializes the Chrome WebDriver (Setup).
    Configures browser options (maximized).
    Navigates to the base URL (https://www.guvi.in/).
    Uses 'yield' to pass the driver to the tests.
    Performs cleanup by quitting the browser after each test (Teardown).
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(2) # Sets a global implicit wait time
    yield driver
    driver.quit() # Closes the browser after the test function is done (Task Requirement: Close the browser)



# Define the test function, which takes the Selenium WebDriver instance as an argument
def test_Swag_Labs(driver):
    """
    Automates the login process for the Swag Labs website and performs
    basic post-login assertions and data saving.
    """
    try:
        # --- 1. Locate Web Elements ---

        # Find the username input field by its ID
        username = driver.find_element(By.ID, "user-name")
        # Find the password input field by its NAME attribute
        password = driver.find_element(By.NAME, "password")
        # Find the login button by its ID
        login = driver.find_element(By.ID, "login-button")

        # --- 2. Perform Login Action ---

        # Enter the standard username into the username field
        username.send_keys("standard_user")
        # Enter the secret password into the password field
        password.send_keys("secret_sauce")
        # Click the login button to submit the credentials
        login.click()

        # Pause execution for 2 seconds to allow the page to load after login
        time.sleep(2)

        # --- 3. Assertion: Check Page Title ---

        # Get the title of the current webpage (should be the 'Products' page after login)
        page_title = driver.title
        # Assert that the retrieved page title matches the expected title
        # If it doesn't match, the test will fail
        assert page_title == "Swag Labs"
        # Print a success message with the retrieved title
        print(f"\n1. Title of the webpage: {page_title}")

        # --- 4. Assertion: Check Current URL ---

        # Get the current URL of the browser
        current_url = driver.current_url
        # Print the current URL (optional, for debugging)
        print(current_url)
        # Define the expected URL for the inventory/products page
        expected_url = 'https://www.saucedemo.com/inventory.html'
        # Assert that the current URL matches the expected inventory URL
        assert current_url == expected_url
        # Print a success message with the current URL
        print(f"2. Current URL: {current_url}")

        # --- 5. Data Saving: Save Page Source to File ---

        # Get the complete HTML source code of the current page
        page_content = driver.page_source
        # Define the filename for the output file
        filename = 'Webpage_task_11.txt'

        # Open the file in write mode ('w') with UTF-8 encoding
        with open(filename, 'w', encoding='utf-8') as f:
            # Write the page title and current URL to the file
            f.write(f'page title: {page_title}\n')
            f.write(f'current url: {current_url}\n')
            f.write(f"\n{'=' * 80}\n")
            f.write(f"Page Source:\n")
            f.write(f"\n{'=' * 80}\n")
            # Write the entire page source (HTML) to the file
            f.write(page_content)
        # Print a message indicating where the content was saved
        print(f"3. Page content saved to: {filename}")

    # --- 6. Error Handling ---

    # Catch any exceptions that occur during the test execution
    except Exception as e:
        # Use pytest.fail to explicitly fail the test and report the error message
        pytest.fail(f"Test failed: {str(e)}")










