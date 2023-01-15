import requests
#*************************************Petfinder API***********************************

# ---------------------------------------Generate token-------------------------------
url = "https://api.petfinder.com/v2/oauth2/token"

payload='grant_type=client_credentials&client_id=bW7OXCaTdgUQDObQNva825OVdnYePKG0OjWVcPRGIqgi2BlGnv&client_secret=BLHjf76w8MKILNNUOoEVdRFgO4PqLTxAD3sUgy8W'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)
finalRes=response.json()
print(finalRes['token_type'])
print(finalRes['expires_in'])
print(finalRes['access_token'])


token_type=finalRes['token_type']
access_token_co=finalRes['access_token']
tok=f'{token_type} {access_token_co}'
# tok2='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJiVzdPWENhVGRnVVFET2JRTnZhODI1T1ZkblllUEtHME9qV1ZjUFJHSXFnaTJCbEdudiIsImp0aSI6ImU1NzRhN2U5YTZmMzNjZjQ0MjkzNmU4YTM2ODI2NWRkNDYzMjk4ZmVhNTUwNzExODZlMjA3NTI5MTg5MWU1MzFiMWY3YWM5NGQ3OWZmMjVkIiwiaWF0IjoxNjczNzkyMjUyLCJuYmYiOjE2NzM3OTIyNTIsImV4cCI6MTY3Mzc5NTg1Miwic3ViIjoiIiwic2NvcGVzIjpbXX0.J6s37rMuSCJkxMLHudcThyk2T2kbQuIAirhKfBc9JiQD0XuCp8ZSaXhjLl3Ji6PatnlsVybyHfFT0KGG6GG0STgN14FBqDGuRnqTd1pJYVAvgZcKPnUQ_wC-_ZeshT3zgbOI7gX1ncw7ue_Jgz1WVycifVr1MF9m0wuUDJKdeKvBlL-Tw8Sj_d8u0tgAOtIUCyEQIu1GQWrxKZHJRQTfobWluI1F9MZSdy7Oi2htCQZkGiPIcA6yKZsSMDw_2K0BkTTteJCUtD4Uex5Fm-E3GLiKEfDb_voWhYVidPp-B13RX0MfTNImbrYShguGDdqreonAmBOozDc-etRFx8bjyQ'
# print(tok2)

# ---------------------------------------Get Dog Breeds-------------------------------


headersTwo = {
    'Authorization': tok,
}

responseTwo = requests.get('https://api.petfinder.com/v2/types/dog/breeds', headers=headersTwo)
breeds=responseTwo.json()
print(breeds)
