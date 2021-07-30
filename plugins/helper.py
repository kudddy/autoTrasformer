from aiohttp_requests import requests
from json import dumps

url = "https://api.sberauto.com/searcher/getCars"


async def get_cars_from_sberauto(brand_id: int, city_id: int, year_to: int = None, year_from: int = None):
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "filter": {
            "engine_type_code": [],
            "transmission_code": [],
            "transmission_drive_code": [],
            "color_code": [],
            "body_type_code": [],
            "label_code": [],
            "city_id": [city_id],
            "is_new": None,
            "catalog": [
                {
                    "brand_id": brand_id,
                    "model_id": [],
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

    response = await requests.post(url, headers=headers, data=dumps(payload), ssl=False)

    response = await response.json()

    return response


def parse_response(resp: dict):
    data = resp.get("success", False)
    search_res = resp.get("data", {}).get("results", [])
    min_price = None
    max_price = None
    count = None

    if data and len(search_res) > 0:
        prices = [x['price'] for x in search_res]
        min_price = max(prices)
        max_price = min(prices)
        count = len(prices)
        status = True
    else:
        status = False

    return status, min_price, max_price, count


def generate_url(brand_id: int, city_id: int) -> str:
    done_url = "https://sberauto.com/cars?brand={}&city={}&rental_car=exclude_rental".format(brand_id, city_id)

    return done_url
