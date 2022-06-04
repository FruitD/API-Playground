import os
import sys

from CodeChef.find_remainder import get_division_remainder
from CodeChef.number_mirror import output_what_is_inputted
from League.worker import get_summoner_data_by_name
from dotenv import load_dotenv, find_dotenv


def run():
    # load_dotenv()
    path = sys.path[0] + '/config/.env'  # try .path[0] if 1 doesn't work
    load_dotenv(find_dotenv(path))
    api_key = os.getenv('API_KEY')
    temp_region = os.getenv('REGION')
    temp_name = 'FruitDDisco'
    get_summoner_data_by_name(api_key, temp_region, temp_name)


if __name__ == '__main__':
    run()
