import requests
import os
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


url = 'https://api.weibo.com/2/statuses/share.json'
access_token = os.getenv('WEIBO_ACCESS_TOKEN')
link = 'https://github.com/Miloas/haha'

msg = '恭喜哈哈，终成万古！' if isAncient() else '没有'

payload = {
    'access_token': access_token,
    'status': f'{msg} {link}'
}

requests.post(url, data=payload)
