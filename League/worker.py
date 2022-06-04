import cassiopeia as cass

api_key = 'RGAPI-cf6ca1c5-e5d3-4e03-93a1-1ac1fa30f4fe'

cass.set_riot_api_key(api_key)

summoner = cass.get_summoner(name="FruitDDisco", region="NA")

items = cass.get_items(region="NA")
for item in items:
    print(item.name)

# def list_all_items():
