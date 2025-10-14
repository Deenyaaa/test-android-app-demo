from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_visibility(driver, locator, timeout = 20):
    wait = WebDriverWait(driver, timeout)
    result = wait.until(EC.visibility_of_element_located((By.ID, locator)))
    return result

def wait_for_clickable(driver, locator, timeout = 20):
    wait = WebDriverWait(driver, timeout)
    result = wait.until(EC.element_to_be_clickable((By.ID, locator)))
    return result