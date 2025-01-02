import requests

url = "https://www.virustotal.com/api/v3/analyses/YTU4ZTQwZThiM2RhM2FjZmFkN2M3ZWQ1MTBmNTBkMzk6MTcwNjc5ODc0OQ=="

headers = {
    "accept": "application/json",
    "x-apikey": "1db433eff16e541be6c8fccdaa9e85ae731a2a60ff60d5268bff87ca85102a61"
}

response = requests.get(url, headers=headers)

print(response.text)