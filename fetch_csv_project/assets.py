import requests
import csv

from dagster import asset

api_key = "M2Z69469HXICTNG2WJC9BC6IWECE3QY2K7"


def fetch_api(contract_address) :
    url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    

@asset
def contract_api_assets():
    contract_addresses = []
    with open("data/address.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contract_addresses.append(row[0])

    apis = []
    for contract_address in contract_addresses:
        api = fetch_api(contract_address)
        if api is not None:
            apis.append(api)
    
    with open("data/fetch_api.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for row in apis:
            writer.writerow(row.values())

    return apis

