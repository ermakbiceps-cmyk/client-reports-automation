from yandex_direct import get_direct_stats
import json


with open("clients.json", "r", encoding="utf-8") as file:
    clients = json.load(file)


client = clients["clients"][0]


result = get_direct_stats(
    client["yandex_token"],
    client["yandex_login"]
)


print(result)
