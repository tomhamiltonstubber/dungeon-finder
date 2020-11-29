from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from models import Game
from settings import Settings
from utils import get_db


async def index(request: Request):
    settings = Settings()
    return settings.templates.TemplateResponse('index.jinja', {'request': request})


async def games_list(request: Request, db: Session = Depends(get_db)):
    settings = Settings()
    games = db.query(Game)
    return settings.templates.TemplateResponse('games/list.jinja', {'request': request, 'games': games})
