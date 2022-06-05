import os
import sys

from dotenv import load_dotenv, find_dotenv

from src.Riot.worker import print_champion_dict, get_all_item_names, get_match_history_data_by_summoner_name


def run():
    path = sys.path[0] + '/config/.env'
    load_dotenv(find_dotenv(path))
    api_key = os.getenv('API_KEY')
    temp_region = os.getenv('REGION')
    temp_name = 'FruitDDisco'

    # get_match_history_data_by_summoner_name(api_key, temp_region, temp_name)
    # get_all_item_names(api_key, temp_region)
    # print_champion_dict(api_key, temp_region)
    print_champion_dict(api_key, temp_region)


if __name__ == '__main__':
    run()
