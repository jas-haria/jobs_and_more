import requests
from datetime import datetime
import pandas as pd
import csv

def get_news_data():
    # put key in config file
    companies = pd.read_csv('../predefined_data/company_list.csv')
    news_items = []
    for symbol in companies['Abbreviation']:
        news_items.extend(call_api(symbol))
    csv_columns = ['symbol', 'headline', 'description', 'published_date', 'url']
    with open('../downloaded_data/cnbc_data', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in news_items:
            writer.writerow(data)
        csvfile.truncate()
        
    
    
def call_api(symbol):
    url = "https://cnbc.p.rapidapi.com/news/v2/list-by-symbol"
    querystring = {"symbol":symbol,"page":"1","pageSize":"5"}
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': "d8cb8f820emsh18db97648694a5bp1920fbjsneab9c02820ba"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = response.json()
    data = []
    for result in json_response['data']['symbolEntries']['results']:
        data_dict = {}
        data_dict['symbol'] = symbol
        data_dict['headline'] = result['headline']
        data_dict['description'] = result['description']
        published_date = datetime.strptime(result['dateLastPublished'][:-14], '%Y-%m-%d')
        data_dict['published_date'] = published_date.strftime('%B %d, %Y')
        data_dict['url'] = result['url']
        data.append(data_dict)
    print(len(data), symbol)
    return data

get_news_data()