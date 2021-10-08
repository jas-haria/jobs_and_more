
input_prompt = '''
1 - Show jobs by city
2 - Show jobs by company
3 - Refresh data
'''


def refresh_stats():
    # get data from csv

    # scrape jobs

    # scrape salaries

    # download tax data

    # scrape house listings

    # get news listing from api
    return None

while True:
    val = input(input_prompt)
    if val == '3':
        refresh_stats()
    else:
        break
