from pydantic import BaseSettings
from starlette.templating import Jinja2Templates


class Settings(BaseSettings):
    templates = Jinja2Templates(directory='../templates')
    debug: bool = False

    class Config:
        fields = {
            'debug': {'env': 'DEBUG'},
        }
