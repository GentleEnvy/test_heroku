import requests

print(requests.get(
    'https://bankrot.fedresurs.ru/TradeList.aspx'
).content)
