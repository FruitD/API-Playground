import cassiopeia as cass


def get_match_history_data_by_summoner_name(api_key, region, name):
    cass.set_riot_api_key(api_key)

    summoner = cass.get_summoner(name=name, region=region)

    print(summoner.match_history)


def get_all_item_names(api_key, region):
    cass.set_riot_api_key(api_key)

    items = cass.get_items(region)
    for item in items:
        print(item.name)


def print_champion_dict(api_key, region):
    cass.set_riot_api_key(api_key)

    champion_dict = cass.get_champions(region)

    for champion in champion_dict:
        print(champion.name)
