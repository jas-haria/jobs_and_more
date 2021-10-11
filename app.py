from apis.cnbc_api import get_news_data
from download_scripts.tax_foundation_downloader import update_tax_data
from scraping_scripts.careerbuilder_scraper import refresh_salaries
from scraping_scripts.dice_scraper import refresh_jobs, test
from scraping_scripts.mynewhome_scraper import refresh_homes

input_prompt = '''
1 - Show jobs by city
2 - Show jobs by company
3 - Refresh data
'''


def refresh_stats():
    test()
    #refresh_jobs()
    #refresh_salaries()
    #refresh_homes()
    #update_tax_data()
    #get_news_data()

if __name__ == '__main__':
    while True:
        val = input(input_prompt)
        if val == '3':
            refresh_stats()
        else:
            break
