from utils.util_service import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
import re

companies = ['Deloitte']
city = ['Los Angeles, CA, USA']

def refresh_jobs():
    links = get_job_urls()
    jobs_data = []
    for link in links:
        jobs_data.append(get_job_from_url(link))

def get_job_urls():
    driver = get_driver()
    links = []
    for company in companies:
        driver.get('https://www.dice.com/')
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'typeaheadInput')]")))
        input.clear()
        input.send_keys(company)
        location = driver.find_element_by_xpath("*//input[contains(@id, 'google-location-search')]")
        location.clear()
        location.send_keys(city)
        time.sleep(1)
        submit = driver.find_element_by_xpath("*//button[contains(@id, 'submitSearch-button')]")
        submit.click()
        time.sleep(3)
        raw_links = driver.find_elements_by_xpath("*//a[contains(@class, 'card-title-link bold')]")
        for link in raw_links:
            links.append(link.get_attribute('href'))
    return links
    

def get_job_from_url(url):
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), "lxml")
    tc = bs.findAll('h1', { "class" : "jobTitle"} )
    job = tc[0].text
    org = bs.findAll('span',{"class":"name"})
    organisation = org[0].text
    loc = bs.findAll('li',{"class":"location"})
    location = loc[0].text
    desc = bs.findAll('div',{"class":"highlight-black"})
    description = desc[0].text
    location = location.replace("\n",'')
    location = location.replace("\t",'')
    description = description.replace("\t","")
    description = description.replace("\n","")
    jobdict = {'title':job,'company':organisation,'location':location,
               'summary':description}
    return jobdict