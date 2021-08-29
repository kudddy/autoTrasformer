from json import dumps
from statistics import median

from aiohttp_requests import requests

from plugins.config import cfg
from plugins.helper import generate_city_str
from persistants.request_info import headers_sberauto

url = cfg.app.url.sberautogetcars


async def get_cars_from_sberauto(brand_id: int or bool,
                                 city_id: list or bool,
                                 model_id: int or bool,
                                 year_to: int or bool,
                                 year_from: int or bool,
                                 page: int):
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
        "per_page": 100,
        "sort_asc": False,
        "sort_by": "",
        "page": page
    }

    response = await requests.post(url, headers=headers_sberauto, data=dumps(payload), ssl=False)

    response = await response.json()

    return response


def parse_response(search_res: list):
    min_price = None
    max_price = None
    middle_value = None
    count = None
    status = False
    if search_res is None:
        return status, min_price, max_price, count

    if len(search_res) > 0:
        prices = [x['price'] for x in search_res]
        min_price = min(prices)
        middle_value = median(prices)
        max_price = max(prices)
        count = len(prices)
        status = True
    else:
        status = False

    return status, min_price, middle_value, max_price, count


def generate_url(brand_id: int,
                 city_id: list,
                 model_id: int,
                 year_from: int,
                 year_to: int) -> str:
    # генерация ссылки относительно входящий параметов
    if brand_id and city_id and model_id:
        city_str = generate_city_str(city_id)
        done_url = "https://sberauto.com/app/cars?brand={}=model={}&rental_car=exclude_rental{}".format(brand_id,
                                                                                                    model_id,
                                                                                                    city_str)
    elif brand_id and model_id:
        done_url = "https://sberauto.com/app/cars?brand={}=model={}&rental_car=exclude_rental".format(brand_id,
                                                                                                  model_id)
    elif brand_id and city_id:
        city_str = generate_city_str(city_id)
        done_url = "https://sberauto.com/app/cars?brand={}{}&rental_car=exclude_rental".format(brand_id,
                                                                                           city_str)
    elif brand_id:
        done_url = "https://sberauto.com/app/cars?brand={}&rental_car=exclude_rental".format(brand_id)
    else:
        done_url = "https://sberauto.com/app/cars?"
    if year_to or year_from:
        if year_to and year_from:
            done_url = done_url + "&dateTo={}&dateFrom={}".format(year_to, year_from)
        elif year_to:
            done_url = done_url + "&dateTo={}".format(year_to)
        elif year_from:
            done_url = done_url + "&dateFrom={}".format(year_from)
    return done_url
