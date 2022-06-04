import os

from CodeChef.find_remainder import get_division_remainder
from CodeChef.number_mirror import output_what_is_inputted
from League.worker import get_summoner_data_by_name
from dotenv import load_dotenv


def run():
    # load_dotenv()
    # api_key = os.getenv('API_KEY')
    # temp_region = os.getenv('REGION')
    temp_name = 'FruitDDisco'
    get_summoner_data_by_name('RGAPI-b4bb24da-9abf-414e-91cf-66f002d15851', 'NA', temp_name)


if __name__ == '__main__':
    run()
