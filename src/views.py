from starlette.requests import Request

from settings import Settings


async def index(request: Request):
    settings = Settings()
    return settings.templates.TemplateResponse('index.jinja', {'request': request})
