from pathlib import Path

from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.responses import HTMLResponse
from starlette.routing import Mount

from settings import Settings
from starlette.staticfiles import StaticFiles

from views import index

THIS_DIR = Path(__file__).parent.resolve()

routes = [
    APIRoute('/', index, name='index', response_class=HTMLResponse),
    Mount('/static', StaticFiles(directory=THIS_DIR / 'static'), name='static'),
]

settings = Settings()
app = FastAPI(debug=settings.debug, routes=routes)
