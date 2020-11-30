from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from src.database import get_db
from src.models import Game
from src.settings import Settings


async def index(request: Request):
    settings = Settings()
    return settings.templates.TemplateResponse('index.jinja', {'request': request})


async def games_list(request: Request, db: Session = Depends(get_db)):
    settings = Settings()
    games = db.query(Game)
    return settings.templates.TemplateResponse('games/list.jinja', {'request': request, 'games': games})
