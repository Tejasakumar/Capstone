import requests
url = "https://api.blockchair.com/bitcoin-cash/dashboards/address/0x388C818CA8B9251b393131C08a736A67ccB19297?key=G___4K6iQ1JPyGiCFPtqNgs923a1hJyk&limit=1"
res = requests.get(url)
print(res.json())
addr_data = res.json()
