import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
class IncorrectPasswordException(Exception):
    pass
chrome_options=Options()
def test_login_1():
    # chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    # driver.maximize_window()
    print(driver.title)
    try:
        user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="username"]')))
        user_name.send_keys("Admin")
        wait = WebDriverWait(driver, 5)
        pass_value = driver.find_element(By.XPATH,
                                         '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        pass_value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')))
        pass_value.send_keys("admin123")
        wait = WebDriverWait(driver, 5)
        time.sleep(5)
        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
        log_in.click()
        # //*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p
        error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')))
        if "Invalid credentials" in error_message.text:  # Adjust the text to match the actual error message
            raise IncorrectPasswordException("Incorrect password provided: " + error_message.text)

        print("Logged into the website")
        time.sleep(8)
    except IncorrectPasswordException as e:
        print(f"Login failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.close()
def test_login_2():
    # chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    # driver.maximize_window()
    print(driver.title)
    try:
        user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="username"]')))
        user_name.send_keys("Admin")
        wait = WebDriverWait(driver, 5)
        pass_value = driver.find_element(By.XPATH,
                                         '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        pass_value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')))
        pass_value.send_keys("Invalid Password")
        wait = WebDriverWait(driver, 5)
        time.sleep(5)
        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
        log_in.click()
        time.sleep(8)
    except Exception as E:
        print(f"An error occured {E}")
    finally:
        driver.close()
def test_login_pin_02():
    # chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    try:
        user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="username"]')))
        user_name.send_keys("Admin")
        wait = WebDriverWait(driver, 5)
        pass_value = driver.find_element(By.XPATH,
                                         '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        pass_value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')))
        pass_value.send_keys("admin123")
        wait = WebDriverWait(driver, 5)
        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
        log_in.click()
        pim_login=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
        pim_login.click()
        time.sleep(8)
        data_modify=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i')))
        data_modify.click()
        time.sleep(7)
        Mid_name=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input')))
        Mid_name.click()
        Mid_name.clear()
        time.sleep(4)
        Mid_name.send_keys("35")
        time.sleep(10)
        submit=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')))
        submit.click()
        time.sleep(7)
        print('Successfull employee details addition')
    except Exception as E:
        print(f"An error occured {E}")
    finally:
        driver.close()
def test_login_pin_03():
    # chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    try:
        user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="username"]')))
        user_name.send_keys("Admin")
        wait = WebDriverWait(driver, 5)
        pass_value = driver.find_element(By.XPATH,
                                         '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        pass_value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')))
        pass_value.send_keys("admin123")
        wait = WebDriverWait(driver, 5)
        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
        log_in.click()
        time.sleep(5)
        delete_ele=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i')))
        delete_ele.click()
        time.sleep(8)
        driver.switch_to_alert().accept()

    except Exception as E:
        print(f"An error occured {E}")
    finally:
        driver.close()




if __name__=="__main__":
    test_login_1()
    test_login_2()
    test_login_pin_02()
    test_login_pin_03()




