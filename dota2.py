from typing import Optional
import requests
import os
import sys

account_id = os.getenv('ACCOUNT_ID')
api_key = os.getenv('OPENDOTA_API_KEY')

if account_id == None or api_key == None:
    sys.exit('script need account_id and api_key')

rank_tier: Optional[str] = requests.get(f'https://api.opendota.com/api/players/{account_id}', params = {
    api_key: api_key
}).json()['rank_tier']

def isAncient():
    return rank_tier != None and int(rank_tier[0]) >= 6

print(isAncient())
