import logging

from aiohttp.web_response import Response
from aiohttp_apispec import docs, response_schema

from .base import BaseView

from plugins.responder.sberauto import generate_url, get_cars_from_sberauto, parse_response
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log.setLevel(logging.INFO)


class CanvasHandler(BaseView):
    URL_PATH = r'/get-canvas-handler/'

    @docs(summary="Возвращает структурированный текст", tags=["Basic methods"],
          description="Ручка анализирут пользовательский запрос и возвращает результат duckling",
          )
    # @response_schema(description="Возвращает n число ближайших соседей токена"
    #                              "сортированные по дате")
    async def post(self):
        # result: dict = {}
        #
        # res: dict = await self.request.json()
        #
        # text: dict = res["data"]["text"]

        status: bool = True

        try:
            logging.info("message_name - %r info - %r", "GET_DUCKLING_RESULT", "token - {}".format("test"))
            # TODO логка реализации duckling и тд. пока формируем заглушку
            # TODO должен вернуть brand_id, model_id, city_id
            # brand_id, city_id = self.model().get_struct_info()

            # response = await get_cars_from_sberauto(brand_id=brand_id, city_id=city_id)

            # status, min_price, max_price, count = parse_response(response)

            # if status:
            #     done_url = generate_url(brand_id, city_id)
            # else:
            #     done_url = None

            return Response(body={"MESSAGE_NAME": "GET_CANVAS_DATA",
                                  "STATUS": status,
                                  "PAYLOAD": {
                                      "result": [
                                        {
                                          "min_price": 4343,
                                          "max_price": 23435135,
                                          "count": 583,
                                          "url": 1235
                                        },
                                        {
                                          "min_price": 345215,
                                          "max_price": 388356,
                                          "count": 43434,
                                          "url": 8282
                                        },
                                        {
                                          "min_price": 5880175,
                                          "max_price": 145435,
                                          "count": 8403157,
                                          "url": 92375924501
                                        },
                                                ],
                                      "description": "OK"
                                  }})
        except Exception as e:
            logging.info("message_name - %r info - %r error - %r",
                         "GET_DUCKLING_RESULT",
                         "token - {}".format("fdfddf"),
                         e)
            status = False
            return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                  "STATUS": status,
                                  "PAYLOAD": {
                                      "result": [],
                                      "description": "error"
                                  }})