from typing import Optional

from pydantic import BaseSettings
from starlette.templating import Jinja2Templates


class Settings(BaseSettings):
    templates = Jinja2Templates(directory='../templates')
    debug: bool = False
    database_url: Optional[str] = 'postgres://postgres@localhost:5432/dungeonfinder'

    class Config:
        fields = {
            'database_url': {'ENV': 'DATABASE_URL'},
            'debug': {'env': 'DEBUG'},
        }
