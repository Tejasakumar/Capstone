# we first have to upload a file it gives us the id corresponding to it
import requests

url = "https://www.virustotal.com/api/v3/files"

files = { "file": ("lex.exe", open("mylex.exe", "rb")) }
headers = {
    "accept": "application/json",
    "x-apikey": "1db433eff16e541be6c8fccdaa9e85ae731a2a60ff60d5268bff87ca85102a61"
}

response = requests.post(url, files=files, headers=headers)

print(response.text)

# this is the id that we have got ZDI4MDIwOWVjYmY4Yjk2MzBiM2JkZGM1MzM2MGE4YTY6MTcwNjEwOTE5Mw==
