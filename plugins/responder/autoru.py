from json import dumps

from aiohttp_requests import requests


from plugins.config import cfg
from plugins.loader import marks, models, citys
from plugins.helper import is_true
from persistants.request_info import headers_auto_ru

url_auto_ru: str = cfg.app.url.autoru


async def get_resp_from_yandex_systems(payload: dict):
    response = await requests.post(url_auto_ru,
                                   headers=headers_auto_ru,
                                   data=dumps(payload),
                                   ssl=False)

    d = await response.json()

    return d


async def get_search_res_yandex(text: str):
    payload = {"category": "cars",
               "query": text,
               "section": "all",
               "geo_radius": 200, "geo_id": [213]}

    data = await get_resp_from_yandex_systems(payload)

    if "catalog_filter" in data['suggests'][0]['params']:

        mark = data['suggests'][0]['params']['catalog_filter'][0].get('mark', False)

        model = data['suggests'][0]['params']['catalog_filter'][0].get('model', False)
    else:
        mark = False

        model = False

    year_from = data['suggests'][0]['originalParams'].get("year_from", False)
    year_to = data['suggests'][0]['originalParams'].get("year_to", False)
    city_id = []
    if "regions" in data['suggests'][0]['view']:
        for region in data['suggests'][0]['view']['regions']:
            city_id.append(region['id'])
    else:
        city_id = False

    # мапим название яндекса на id сберавто
    # TODO поправить неправильное обозначение
    if mark:
        mark = models.get(mark, False)

    if model:
        model = marks.get(model, False)
    if city_id:
        city_id = [citys.get(x, False) for x in city_id]

        city_id = list(filter(is_true, city_id))

        if len(city_id) == 0:
            city_id = False

    return mark, model, city_id, year_from, year_to
