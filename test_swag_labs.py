import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
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


def test_Swag_Labs(driver):
    try:
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.NAME, "password")
        login = driver.find_element(By.ID, "login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login.click()

        time.sleep(2)

        page_title = driver.title
        assert page_title == "Swag Labs"
        print(f"\n1. Title of the webpage: {page_title}")


        current_url = driver.current_url
        print(current_url)
        expected_url = 'https://www.saucedemo.com/inventory.html'
        assert current_url == expected_url
        print(f"2. Current URL: {current_url}")

        page_content = driver.page_source
        filename = 'Webpage_task_11.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'page title: {page_title}\n')
            f.write(f'current url: {current_url}\n')
            f.write(f"\n{'=' * 80}\n")
            f.write(f"Page Source:\n")
            f.write(f"\n{'=' * 80}\n")
            f.write(page_content)
        print(f"3. Page content saved to: {filename}")
    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")












