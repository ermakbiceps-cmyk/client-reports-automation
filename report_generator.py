import json
from datetime import datetime


def load_clients():
    with open("clients.json", "r", encoding="utf-8") as file:
        return json.load(file)


def generate_reports():
    clients = load_clients()

    date = datetime.now().strftime("%d.%m.%Y")

    print("Формирование отчетов:", date)

    for client in clients["clients"]:
        print("Создаем отчет:", client["name"])


if __name__ == "__main__":
    generate_reports()
