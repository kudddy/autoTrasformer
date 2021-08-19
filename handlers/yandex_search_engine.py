import logging
import asyncio

from aiohttp.web_response import Response
from aiohttp_apispec import docs, response_schema
from asyncio import get_event_loop

from plugins.helper import get_cars_from_sberauto, parse_response, generate_url, get_search_res_yandex
from plugins.duckling.typonder import replace_typos

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

        # uid: str = res.get("uid", "")
        #
        # if uid != cfg.app.token:
        #     return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
        #                           "STATUS": False,
        #                           "PAYLOAD": {
        #                               "result": [],
        #                               "description": "wrong uid"
        #                           }})

        text: str = res["data"]["text"]

        # исправляем ошибки
        text = replace_typos(text)

        try:
            logging.info("message_name - %r info - %r", "GET_DUCKLING_RESULT", "token - {}".format(text))

            brand_id, model_id, city_id, year_from, year_to = await get_search_res_yandex(text)

            # TODO подумать насчет этого условия

            if brand_id or model_id or city_id:
                # запускаем локальный цикл событий

                loop_local = get_event_loop()

                async_tasks = []
                for page in range(30):
                    async_tasks.append(loop_local.create_task(
                        get_cars_from_sberauto(brand_id=brand_id,
                                               city_id=city_id,
                                               model_id=model_id,
                                               year_from=year_from,
                                               year_to=year_to,
                                               page=page)
                    ))

                responses = await asyncio.gather(*async_tasks)

                all_responses: list = []
                for data in responses:
                    success = data.get("success")
                    if success:
                        response = data.get("data", {}).get("results", [])
                        if response:
                            all_responses.extend(response)

            else:
                status = False
                return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                      "STATUS": status,
                                      "PAYLOAD": {
                                          "result": result,
                                          "description": "nothing found"
                                      }})

            status, min_price, middle_value, max_price, count = parse_response(all_responses)

            # TODO возможно стоит сделать посимпатичней
            if status:
                done_url = generate_url(brand_id,
                                        city_id,
                                        model_id,
                                        year_from,
                                        year_to)
            else:
                done_url = "https://sberauto.com/cars?"

            print(done_url)

            return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                  "STATUS": status,
                                  "PAYLOAD": {
                                      "result": {
                                          "min_price": min_price,
                                          "median": int(middle_value),
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
