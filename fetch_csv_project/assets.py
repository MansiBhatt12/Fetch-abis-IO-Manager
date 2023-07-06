import requests
import csv
import os
from dagster import asset

api_key = "M2Z69469HXICTNG2WJC9BC6IWECE3QY2K7"

def fetch_api(contract_address):
    url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()

class CSVIOManager:
    def __init__(self, path):
        self.path = path

    def read(self, filename):
        with open(os.path.join(self.path, filename), "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            return [row for row in reader]

    def write(self, filename, data):
        with open(os.path.join(self.path, filename), "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerows(data)

@asset
def contract_api_assets():
    io_manager = CSVIOManager("data")
    contract_addresses = io_manager.read("address.csv")

    # contract_addresses = []
    # with open("data/address.csv", "r") as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         contract_addresses.append(row[0])

    apis = []
    for contract_address in contract_addresses:
        api = fetch_api(contract_address[0]) 
        if api is not None:
            apis.append(api)
            
    # with open("data/five-address-api.csv", "w") as csvfile:
    #     writer = csv.writer(csvfile, delimiter=",")
    #     for row in apis:
    #         writer.writerow(row.values())

    io_manager.write("fetch_api.csv", [row.values() for row in apis])

    return apis
