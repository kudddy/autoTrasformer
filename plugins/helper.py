import logging
from aiohttp_requests import requests
from json import dumps

from persistants.request_info import headers_auto_ru, headers_sberauto
from plugins.loader import marks, models, citys
from plugins.config import cfg

url = cfg.app.url.sberautogetcars

url_auto_ru: str = cfg.app.url.autoru

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log.setLevel(logging.INFO)


def is_true(val):
    if val:
        return val


def generate_city_str(citys_id: list):
    city_str = ""
    for city in citys_id:
        city_str += "&city={}".format(city)
    return city_str


async def get_resp_from_yandex_systems(payload: dict):
    response = await requests.post(url_auto_ru,
                                   headers=headers_auto_ru,
                                   data=dumps(payload),
                                   ssl=False)

    res = await response.text()

    logging.info("request info from yandex - {}".format(res))

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


async def get_cars_from_sberauto(brand_id: int or bool,
                                 city_id: list or bool,
                                 model_id: int or bool,
                                 year_to: int or bool,
                                 year_from: int or bool):
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
            "city_id": city_id if city_id else [],
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
                 city_id: list,
                 model_id: int,
                 year_from: int,
                 year_to: int) -> str:
    # генерация ссылки относительно входящий параметов
    if brand_id and city_id and model_id:
        city_str = generate_city_str(city_id)
        done_url = "https://sberauto.com/cars?brand={}=model={}&rental_car=exclude_rental{}".format(brand_id,
                                                                                                    model_id,
                                                                                                    city_str)
    elif brand_id and model_id:
        done_url = "https://sberauto.com/cars?brand={}=model={}&rental_car=exclude_rental".format(brand_id,
                                                                                                  model_id)
    elif brand_id and city_id:
        city_str = generate_city_str(city_id)
        done_url = "https://sberauto.com/cars?brand={}&city={}&rental_car=exclude_rental".format(brand_id,
                                                                                                 city_str)
    elif brand_id:
        done_url = "https://sberauto.com/cars?brand={}&rental_car=exclude_rental".format(brand_id)
    else:
        done_url = "https://sberauto.com/cars?"
    if year_to or year_from:
        if year_to and year_from:
            done_url = done_url + "&dateTo={}&dateFrom={}".format(year_to, year_from)
        elif year_to:
            done_url = done_url + "&dateTo={}".format(year_to)
        elif year_from:
            done_url = done_url + "&dateFrom={}".format(year_from)
    return done_url
