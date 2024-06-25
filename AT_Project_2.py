import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class IncorrectPasswordException(Exception):
    pass


# Setup Chrome options
chrome_options = Options()


@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


def test_reset_password(driver):
    # Navigate to the login page
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    try:
        # Enter username
        user_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@name="username"]'))
        )
        user_name.send_keys("Admin")

        # Click on 'Forgot your password?' link
        forget_password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'))
        )
        forget_password.click()

        # Enter username to reset
        user_name_to_reset = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input'))
        )
        user_name_to_reset.send_keys("Admin")

        # Click on 'Reset Password' button
        reset_pass = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'))
        )
        reset_pass.click()
        # Assert success message or behavior
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/h6'))
        )
        assert "Reset Password link sent successfully" in success_message.text

    except Exception as e:
        pytest.fail(f"An error occurred: {e}")
    finally:
        driver.close()

    def validate_menu_options():
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        try:
            user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="username"]')))
            user_name.send_keys("Admin")

            pass_value = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@name="password"]')))
            pass_value.send_keys("admin123")

            log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]')))
            log_in.click()

            # Wait for the Admin menu link to be clickable
            admin_menu_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
            )
            admin_menu_link.click()

            # Allow some time for the Admin submenu to expand (adjust as needed)
            time.sleep(3)

            # Define expected menu options with their corresponding XPaths
            expected_options = {
                "User Management": '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span',
                "Job": '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span',
                "Organization": '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span',
                "Qualifications": '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span',
                "Nationalities": '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a',
                "Corporate Banking": '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a',
                "Configuration": '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span'
            }

            missing_options = []

            try:
                # Wait until the page is fully loaded by waiting for a key element, like the Admin menu container
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header'))
                )

                for option, xpath in expected_options.items():
                    try:
                        # Wait for the specific menu option to be present
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, xpath))
                        )
                        print(f"Option '{option}' is present.")
                    except Exception as e:
                        missing_options.append(option)
                        print(f"Option '{option}' is missing. Error: {e}")

                # Print missing options
                if missing_options:
                    print(f"Missing Options: {missing_options}")
                else:
                    print("All expected options are present.")

            except Exception as e:
                print(f"An error occurred during menu validation: {e}")

        finally:
            # Close the WebDriver session
            driver.quit()

    def validate_menu_options_1():
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        try:
            user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="username"]')))
            user_name.send_keys("Admin")

            pass_value = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@name="password"]')))
            pass_value.send_keys("admin123")

            log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]')))
            log_in.click()
            # Define expected menu options with their corresponding XPaths
            expected_options = {
                "Admin": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a',
                "PIM": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span',
                "Leave": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a',
                "Time": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a',
                "Recruitment": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span',
                "My Info": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a',
                "Performance": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a',
                "Dashboard": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a',
                "Directory": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a',
                "Maintanence": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span',
                "Buzz": '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span'
            }

            missing_options = []

            try:

                for option, xpath in expected_options.items():
                    try:
                        # Wait for the specific menu option to be present
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, xpath))
                        )
                        print(f"Option '{option}' is present.")
                    except Exception as e:
                        missing_options.append(option)
                        print(f"Option '{option}' is missing. Error: {e}")

                # Print missing options
                if missing_options:
                    print(f"Missing Options: {missing_options}")
                else:
                    print("All options are present.")

            except Exception as e:
                print(f"An error occurred during menu validation: {e}")

        finally:
            # Close the WebDriver session
            driver.quit()

    if __name__ == "__main__":
        # calling the function
        pytest.main([__file__, "-s"])
        validate_menu_options()
        validate_menu_options_1()


