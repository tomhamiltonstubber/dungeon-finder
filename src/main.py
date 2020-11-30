from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.responses import HTMLResponse
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from src import views
from src.database import prepare_database
from src.logs import setup_logging
from src.settings import Settings

THIS_DIR = Path(__file__).parent.resolve()

routes = [
    APIRoute('/', views.index, name='index', response_class=HTMLResponse),
    APIRoute('/list/', views.games_list, name='index', response_class=HTMLResponse),
    Mount('/static', StaticFiles(directory=THIS_DIR / 'static'), name='static'),
]

settings = Settings()

engine = prepare_database(delete_existing=False, settings=settings)
app = FastAPI(debug=settings.debug, routes=routes)
setup_logging()


# For running locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
