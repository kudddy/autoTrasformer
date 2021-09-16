import requests
import json

url = "https://auto.ru/-/ajax/desktop/searchlineSuggest/"

payload = json.dumps({
  "category": "",
  "query": "хочу бмв 3",
  "section": "all",
  "geo_radius": 200,
  "geo_id": [
    239
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'X-Vertis-DC=sas; _ym_d=1628247925; _ym_uid=1627652375217728242; from=direct; from_lifetime=1628247925149; _ga=GA1.2.78485480.1627652393; _gid=GA1.2.1761382875.1628247834; counter_ga_all7=2; _ym_isad=2; autoru_sid=a%3Ag610401122aqdp79ib94l5jgaoo8dd5e.82824d36cb05580ff796d7838e23aac6%7C1628257170293.604800.7V5UeZCHjvrEpErMEPEaVw.qHK0QnNtWWNBg6_LaVe5kvivcBF7SVX6LV96wiijrII; cycada=wSHPJILwhMUqfY+HsSRIeoYqcwM/ywaWEp8N9/2VJNI=; gdpr=0; _csrf_token=8abf8380c0909f680b8b269c8f485c65e7986f28628f0e61; autoruuid=g610401122aqdp79ib94l5jgaoo8dd5e.82824d36cb05580ff796d7838e23aac6; my=YwA%3D; suid=a6c7a4306035d4fa9972de79a8e5a3fe.a4d5a7c2204edf7436640046e69f4d80; yandexuid=6792294961603390603; yuidlt=1; X-Vertis-DC=sas; _ym_d=1631012422; _ym_uid=1627652375217728242; autoru_sid=a%3Ag610401122aqdp79ib94l5jgaoo8dd5e.82824d36cb05580ff796d7838e23aac6%7C1631012422768.604800.Ix9TNttOpucS_-hrrelJjw.o_RDr4E2F_haUz6fcn2HuFwAHwArUi4FK3lNHwKUC8c; from=direct; from_lifetime=1631012422753',
  'x-client-date': '1628247927314',
  'x-requested-with': 'fetch',
  'x-page-request-id': 'b05d9af6ca95421089b2513de9ffdb18',
  'x-client-app-version': '19b33dfade3',
  'x-csrf-token': '8abf8380c0909f680b8b269c8f485c65e7986f28628f0e61',
  'Connection': 'keep-alive',
  'Referer': 'https://auto.ru/',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
  'Origin': 'https://auto.ru'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
