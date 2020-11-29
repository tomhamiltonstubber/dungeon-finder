from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRoute

from starlette.responses import HTMLResponse
from starlette.routing import Mount

import views
from database import Base, engine
from settings import Settings
from starlette.staticfiles import StaticFiles

THIS_DIR = Path(__file__).parent.resolve()

routes = [
    APIRoute('/', views.index, name='index', response_class=HTMLResponse),
    APIRoute('/list/', views.games_list, name='index', response_class=HTMLResponse),
    Mount('/static', StaticFiles(directory=THIS_DIR / 'static'), name='static'),
]

settings = Settings()

Base.metadata.create_all(bind=engine)
app = FastAPI(debug=settings.debug, routes=routes)


# For running locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
