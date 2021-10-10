from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito");
    path = r"C:/Users/jasha/DFP/jobs_and_more/chromedriver/chromedriver.exe"
    driver = webdriver.Chrome(path, options=options)
    driver.maximize_window()
    return driver