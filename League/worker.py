import cassiopeia as cass
from cassiopeia import Summoner

temp_name = "FruitDDisco"


def get_summoner_data_by_name(api_key, region, name):
    cass.set_riot_api_key(api_key)

    summoner = cass.get_summoner(name=name, region=region)

    print(summoner.account_id)
    # items = cass.get_items(region)
    # for item in items:
    #     print(item.name)

    # def list_all_items():
