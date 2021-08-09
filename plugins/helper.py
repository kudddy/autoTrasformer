from aiohttp_requests import requests
from json import dumps

from persistants.request_info import headers_auto_ru, headers_sberauto
from plugins.loader import marks, models, citys

# TODO вынести в конфиг
url = "https://api.sberauto.com/searcher/getCars"

url_auto_ru: str = "https://auto.ru/-/ajax/desktop/searchlineSuggest/"


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

    if "regions" in data['suggests'][0]['view']:
        city_id = data['suggests'][0]['view']['regions'][0]['id']
    else:
        city_id = False

    # мапим название яндекса на id сберавто
    # TODO поправить неправильное обозначение
    if mark:
        mark = models[mark]

    if model:
        model = marks[model]

    if city_id:
        city_id = citys[city_id]

    return mark, model, city_id, year_from, year_to


async def get_cars_from_sberauto(brand_id: int or bool,
                                 city_id: int or bool,
                                 model_id: int or bool,
                                 year_to: int,
                                 year_from: int):
    payload = {
        "filter": {
            "engine_type_code": [],
            "transmission_code": [],
            "transmission_drive_code": [],
            "color_code": [],
            "body_type_code": [],
            "label_code": [],
            "year_to": year_to if year_to else None,
            "year_from": year_from if year_from else None,
            "city_id": [city_id] if city_id else [],
            "is_new": None,
            "catalog": [
                {
                    "brand_id": brand_id,
                    "model_id": [model_id] if model_id else [],
                    "folder_id": []
                }
            ],
            "rental_car": "exclude_rental"
        },
        "per_page": 1000,
        "sort_asc": False,
        "sort_by": "",
        "page": 1
    }

    response = await requests.post(url, headers=headers_sberauto, data=dumps(payload), ssl=False)

    response = await response.json()

    return response


def parse_response(resp: dict):
    data = resp.get("success", False)
    search_res = resp.get("data", {}).get("results", [])

    min_price = None
    max_price = None
    count = None
    status = False
    if search_res is None:
        return status, min_price, max_price, count

    if data and len(search_res) > 0:
        prices = [x['price'] for x in search_res]
        min_price = max(prices)
        max_price = min(prices)
        count = len(prices)
        status = True
    else:
        status = False

    return status, min_price, max_price, count


def generate_url(brand_id: int,
                 city_id: int,
                 model_id: int,
                 year_from: int,
                 year_to: int) -> str:
    # генерация ссылки относительно входящий параметов
    # https: // sberauto.com / cars?brand = 229 = model = 2781 & city = 1 & dateTo = 2021 & dateFrom = 2018 & rental_car = exclude_rental
    if brand_id and city_id and model_id:
        done_url = "https://sberauto.com/cars?brand={}=model={}&city={}&rental_car=exclude_rental".format(brand_id,
                                                                                                          model_id,
                                                                                                          city_id)
    elif brand_id and model_id:
        done_url = "https://sberauto.com/cars?brand={}=model={}&rental_car=exclude_rental".format(brand_id,
                                                                                                  model_id)
    elif brand_id and city_id:
        done_url = "https://sberauto.com/cars?brand={}&city={}&rental_car=exclude_rental".format(brand_id,
                                                                                                 city_id)

    elif brand_id:
        done_url = "https://sberauto.com/cars?brand={}&rental_car=exclude_rental".format(brand_id)
    else:
        done_url = "https://sberauto.com/cars?"

    # TODO подумать над этим
    if year_to or year_from:
        if year_to == year_from:
            done_url = done_url + "&dateTo={}".format(year_from)
        else:
            done_url = done_url + "&dateTo={}&dateFrom={}".format(year_to, year_to)

    return done_url
