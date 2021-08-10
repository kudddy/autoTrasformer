import logging

from aiohttp.web_response import Response
from aiohttp_apispec import docs, response_schema

from plugins.helper import get_cars_from_sberauto, parse_response, generate_url, get_search_res_yandex

from .base import BaseView

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log.setLevel(logging.INFO)


class YdxSearchEngine(BaseView):
    URL_PATH = r'/get-search-res-from-yandex/'

    @docs(summary="Возвращает структурированный текст преобразованный серверами yandex", tags=["Basic methods"],
          description="Ручка анализирут пользовательский запрос и возвращает результат duckling",
          )
    async def post(self):
        result: dict = {}

        res: dict = await self.request.json()

        text: str = res["data"]["text"]

        try:
            logging.info("message_name - %r info - %r", "GET_DUCKLING_RESULT", "token - {}".format(text))

            brand_id, model_id, city_id, year_from, year_to = await get_search_res_yandex(text)

            # TODO подумать насчет этого условия

            if brand_id or model_id or city_id:
                response = await get_cars_from_sberauto(brand_id=brand_id,
                                                        city_id=city_id,
                                                        model_id=model_id,
                                                        year_from=year_from,
                                                        year_to=year_to)
            else:
                status = False
                return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                      "STATUS": status,
                                      "PAYLOAD": {
                                          "result": result,
                                          "description": "nothing found"
                                      }})

            status, min_price, max_price, count = parse_response(response)

            # TODO возможно стоит сделать посимпатичней
            if status:
                done_url = generate_url(brand_id,
                                        city_id,
                                        model_id,
                                        year_from,
                                        year_to)
            else:
                done_url = "https://sberauto.com/cars?"

            return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                  "STATUS": status,
                                  "PAYLOAD": {
                                      "result": {
                                          "min_price": min_price,
                                          "max_price": max_price,
                                          "count": count,
                                          "url": done_url
                                      },
                                      "description": "OK"
                                  }})
        except Exception as e:
            logging.info("message_name - %r info - %r error - %r",
                         "GET_DUCKLING_RESULT",
                         "token - {}".format(text),
                         e)
            status = False
            return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                  "STATUS": status,
                                  "PAYLOAD": {
                                      "result": result,
                                      "description": "error"
                                  }})
