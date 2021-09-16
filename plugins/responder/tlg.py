import json
import logging

from aiohttp_requests import requests

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)


async def send_message(url: str,
                       chat_id: int,
                       text: str,
                       parse_mode: str = None,
                       buttons: list or None = None,
                       inline_keyboard: list or None = None,
                       one_time_keyboard: bool = True,
                       resize_keyboard: bool = True,
                       remove_keyboard: bool = False):
    payload = {
        "chat_id": chat_id,
        "text": text[:4095],
        "reply_markup": {
            "remove_keyboard": remove_keyboard
        }
    }

    if parse_mode:
        payload.update({"parse_mode": parse_mode})

    if buttons:
        # TODO hardcode
        keyboards = [[{"text": text}] for text in buttons]
        payload["reply_markup"].update({
            "keyboard": keyboards,
            "resize_keyboard": resize_keyboard,
            "one_time_keyboard": one_time_keyboard
        })

    if inline_keyboard:
        payload["reply_markup"].update({"inline_keyboard": inline_keyboard})

    headers = {
        "Content-Type": "application/json"
    }
    # не дожидаемся ответа чтобы не терять время
    await requests.get(url, headers=headers, data=json.dumps(payload), ssl=False)
    # маскирование текста
    payload["text"] = "*******"

    log.debug("request with payload: %s success delivered to tlg", payload)
