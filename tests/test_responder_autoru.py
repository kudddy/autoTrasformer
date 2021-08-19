import asynctest
import asyncio

from plugins.responder.autoru import get_search_res_yandex
from plugins.responder.sberauto import get_cars_from_sberauto
from plugins.config import cfg


class ResponderTest(asynctest.TestCase):
    async def test_auto_ru_api(self):
        text = "бэха треха в москве"
        brand_id, model_id, city_id, year_from, year_to = await get_search_res_yandex(text)

        self.assertEqual(brand_id, 48)

        self.assertEqual(model_id, False)

        self.assertEqual(city_id, [1])

        self.assertEqual(year_from, False)

        self.assertEqual(year_to, False)

    async def test_sber_auto_ru_api(self):
        brand_id = 48
        model_id = False
        city_id = [1]
        year_from = False
        year_to = False

        loop_local = asyncio.get_event_loop()

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
            self.assertEqual(success, True)
            if success:
                response = data.get("data", {}).get("results", [])
                if response:
                    all_responses.extend(response)

        if len(all_responses) > 0:
            counter = True
        else:
            counter = False

        self.assertEqual(counter, True)




