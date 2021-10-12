from apis.cnbc_api import get_news_data
from download_scripts.tax_foundation_downloader import update_tax_data
from scraping_scripts.careerbuilder_scraper import refresh_salaries
from scraping_scripts.dice_scraper import refresh_jobs
from scraping_scripts.mynewhome_scraper import refresh_homes

input_prompt = '''
1 - Show jobs by city
2 - Show jobs by company
3 - Refresh data
'''


def refresh_stats():
    print('Scraping jobs from dice.com ...')
    refresh_jobs()
    print('Scraping salaries from careerbuilder.com ...')
    refresh_salaries()
    print('Scraping house rentals from mynewhome.com ...')
    refresh_homes()
    print('Downloading tax data from taxfoundation.com ...')
    update_tax_data()
    print('Fetching financial news from cnbc api ...')
    get_news_data()
    print('All data successfully updated!')

if __name__ == '__main__':
    while True:
        val = input(input_prompt)
        if val == '3':
            refresh_stats()
        else:
            break
