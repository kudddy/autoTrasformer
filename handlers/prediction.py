import logging

from aiohttp.web_response import Response
from aiohttp_apispec import docs, response_schema

from .base import BaseView

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log.setLevel(logging.INFO)


class PredictionHandler(BaseView):
    URL_PATH = r'/getnearesttoken/'

    @docs(summary="Возвращает структурированный текст", tags=["Basic methods"],
          description="Ручка анализирут пользовательский запрос и возвращает результат duckling",
          )
    # @response_schema(description="Возвращает n число ближайших соседей токена"
    #                              "сортированные по дате")
    async def post(self):
        status: bool = True
        result: dict = {}

        res: dict = await self.request.json()

        text: dict = res["data"]["text"]

        try:
            logging.info("message_name - %r info - %r", "GET_DUCKLING_RESULT", "token - {}".format(text))
            # TODO логка реализации duckling и тд. пока формируем заглушку
            result = self.model().get_struct_info()

            return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                  "STATUS": status,
                                  "PAYLOAD": {
                                      "result": result,
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
