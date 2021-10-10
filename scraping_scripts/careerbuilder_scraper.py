from bs4 import BeautifulSoup
from utils.util_service import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv

# get company and location from dice data, no location for remote and 0 value?

def refresh_salaries():
    dice_data = pd.read_csv('../downloaded_data/dice_data')
    companies = []
    for index, row in dice_data.iterrows():
        company_dict = {}
        company_dict['company'] = row['company']
        company_dict['title'] = row['title']
        company_dict['location'] = row['location']
        companies.append(company_dict)
    for company in companies:
        driver = get_driver()
        driver.get('https://www.careerbuilder.com/salary')
        wait = WebDriverWait(driver, 3)
        keyword = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'keywords')]")))
        keyword.clear()
        keyword.send_keys(company['company'] + " " + company['title'])
        loc = driver.find_element_by_id('location-searched')
        loc.clear()
        loc.send_keys(company['location'])
        submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id, 'sbmt')]")))
        submit.click()
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        sal = soup.findAll('div', { "class" : "fl-l"} )
        salary = sal[0].text
        company['salary'] = salary
        driver.quit()
    csv_columns = ['title', 'company', 'location', 'salary']
    with open('../downloaded_data/career_builder_data', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in companies:
            writer.writerow(data)
        csvfile.truncate()

print(refresh_salaries())
