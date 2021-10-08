from utils.util_service import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

company = 'Deloitte'
city = 'Los Angeles, CA, USA'

def refresh_jobs():
    driver = get_driver()
    driver.get('https://www.dice.com/')
    wait = WebDriverWait(driver, 3)
    time.sleep(3)
    input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'typeaheadInput')]")))
    input.send_keys(company)
    location = driver.find_element_by_xpath("*//input[contains(@id, 'google-location-search')]")
    location.send_keys(city)
    submit = driver.find_element_by_xpath("*//button[contains(@id, 'submitSearch-button')]")
    submit.click()
    
refresh_jobs()