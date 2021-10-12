import pandas as pd
from utils.util_service import decode_dictionary

def get_average_rent(city, num_of_beds):
    my_new_place_data = pd.read_csv('downloaded_data/mynewhome_data.csv')
    results_df = my_new_place_data[(my_new_place_data['City'] == city) 
                                  and (my_new_place_data['NumOfBed'] == num_of_beds)
                                  and (my_new_place_data['Price'] > 0)]
    return results_df['Price'].mean()

def get_rental_options(city, num_of_beds):
    my_new_place_data = pd.read_csv('downloaded_data/mynewhome_data.csv')
    results_df = my_new_place_data[(my_new_place_data['City'] == city) 
                                  and (my_new_place_data['NumOfBed'] == num_of_beds)]
    rental_options = []
    for index, row in results_df.iterrows():
        option = decode_dictionary(row)
        rental_options.append(option)
    return rental_options
