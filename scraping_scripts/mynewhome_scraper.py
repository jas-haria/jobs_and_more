from utils.util_service import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



urlPrefix = 'https://www.mynewplace.com'
apartmentPrefix = '/apartments-for-rent/'
cities = ['new-york-ny', 'los-angeles-ca']

def refresh_homes():
    for city in cities:
        driver = get_driver()
        driver.get(urlPrefix)
        wait = WebDriverWait(driver, 3)
        arrow = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'arrow')]")))
        arrow.click()
        time.sleep(3)
        cityLink = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '" + str(apartmentPrefix + city) + "')]")))
        cityLink.click()
        time.sleep(3)
        for i in range(1, 4):
            filter = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@onclick, 'toggleFilter()')]")))
            filter.click()
            select = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id, 'beds')]")))
            select.click()
            option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[contains(@value, "+ str(i) +")]")))
            option.click()
            time.sleep(2)
            update = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'submit')]")))
            update.click()
            time.sleep(3)
        driver.quit()
    
refresh_homes()
# check if cities mentioned below get clicked