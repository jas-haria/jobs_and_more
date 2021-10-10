from urllib.request import urlopen
from bs4 import BeautifulSoup
from utils.util_service import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


companies = ['Google LLC Software Engineer']
locations = ['Los Angeles, CA']
# get company and location from dice data, no location for remote and 0 value?

def refresh_salaries():
    driver = get_driver()
    salaries = []
    for company in companies:
        for location in locations:
            driver.get('https://www.careerbuilder.com/salary')
            wait = WebDriverWait(driver, 3)
            keyword = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'keywords')]")))
            keyword.clear()
            keyword.send_keys(company)
            loc = driver.find_element_by_id('location-searched')
            loc.clear()
            loc.send_keys(location)
            submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id, 'sbmt')]")))
            submit.click()
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            sal = soup.findAll('div', { "class" : "fl-l"} )
            salary = sal[0].text
            job_title = soup.findAll('h1')
            org_job_loc = job_title[0].text.strip('\n')
            org_job_loc_list = org_job_loc.split()
            company = org_job_loc_list[3]
            index_in = org_job_loc_list.index('in')
            job_title = ' '.join(org_job_loc_list[4:index_in])
            location = ' '.join(org_job_loc_list[index_in+1:])
            data_dict = {'Company': company, 'Job Title': job_title, 
              'Location': location, 'Salary': salary}
            salaries.append(data_dict)
    return salaries

print(refresh_salaries())
