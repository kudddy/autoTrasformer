import logging
import asyncio

from aiohttp.web_response import Response
from aiohttp_apispec import docs

from plugins.responder.sberauto import get_cars_from_sberauto, \
    parse_response, generate_url, \
    generate_url_for_mobile, generate_text_form
from plugins.responder.autoru import get_search_res_yandex
from plugins.responder.tlg import send_message
from plugins.duckling.typonder import replace_typos
from plugins.config import cfg

from .base import BaseView

tlg_logger = cfg.app.url.tlg

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
        search_res_text_from = None
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

                async_tasks = []
                for page in range(1, 30):
                    async_tasks.append(get_cars_from_sberauto(
                        brand_id=brand_id,
                        city_id=city_id,
                        model_id=model_id,
                        year_from=year_from,
                        year_to=year_to,
                        page=page
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

                logger_string: str = "☢️ по токету - {} ничего не найдено".format(text)
                await send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
                return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                      "STATUS": status,
                                      "PAYLOAD": {
                                          "result": result,
                                          "description": "nothing found"
                                      }})

            status, min_price, middle_value, max_price, count = parse_response(all_responses)

            # проверяем статус от сберавто по поводу найденых авто
            if status:
                if cfg.app.main.redirect_to_mobile:
                    done_url = generate_url_for_mobile(brand_id,
                                                       city_id,
                                                       model_id,
                                                       year_from,
                                                       year_to)
                else:
                    done_url = generate_url(brand_id,
                                            city_id,
                                            model_id,
                                            year_from,
                                            year_to)
                # генерируем текстовую форму

                search_res_text_from = generate_text_form(brand_id,
                                                          city_id,
                                                          model_id,
                                                          year_from,
                                                          year_to)

            else:
                if cfg.app.main.redirect_to_mobile:
                    done_url = "https://sberauto.com/app/chat/car_select"
                else:
                    done_url = "https://sberauto.com/cars?"

            # TODO слишком влияет на производительность
            logger_string: str = "✅по токету - {} OK".format(text)
            await send_message(url=tlg_logger, text=logger_string, chat_id=81432612)

            return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                  "STATUS": status,
                                  "PAYLOAD": {
                                      "result": {
                                          "min_price": min_price,
                                          "median": int(middle_value) if middle_value else None,
                                          "max_price": max_price,
                                          "count": count,
                                          "url": done_url,
                                          "search_text_form": search_res_text_from if search_res_text_from else False,
                                          "search_keys": {
                                              "brand_id": brand_id,
                                              "city_id": city_id,
                                              "model_id": model_id,
                                              "year_from": year_from,
                                              "year_to": year_to
                                          },
                                          # TODO надо что то придумать с пагинацией
                                          "canvas_data": all_responses[:10]
                                      },
                                      "description": "OK"
                                  }})
        except Exception as e:
            logging.info("message_name - %r info - %r error - %r",
                         "GET_DUCKLING_RESULT",
                         "token - {}".format(text),
                         e)
            status = False
            logger_string: str = "🛑 по токету - {} ошибка - {}".format(text, str(e)[0:4095])
            await send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
            return Response(body={"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                                  "STATUS": status,
                                  "PAYLOAD": {
                                      "result": result,
                                      "description": "error"
                                  }})
