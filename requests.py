import requests
deck = requests.get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()

print(deck['deck_id'])
print(deck['remaining'])

for key,value in deck:
    print(f"Key={key}, Value={value}")
