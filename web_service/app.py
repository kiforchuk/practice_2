from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec

from .views.common import index_handler, ping_handler


async def init_app():
    app = web.Application()

    setup_aiohttp_apispec(
        app,
        title='Web Application',
        url='/spec.json',
        swagger_path='/swagger'
    )

    app.router.add_get('/', index_handler)
    app.router.add_get('/ping', ping_handler, allow_head=False)
    return app
