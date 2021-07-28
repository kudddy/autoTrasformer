#! /usr/bin/env python

from aiohttp.web import run_app
from app import create_app

from plugins.config import cfg


if __name__ == '__main__':
    app = create_app()
    run_app(app, host=cfg.app.main.host, port=cfg.app.main.port)
