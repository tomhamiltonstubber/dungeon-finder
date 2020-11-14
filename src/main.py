from fastapi import FastAPI

from settings import Settings
from starlette.requests import Request
from starlette.responses import HTMLResponse

settings = Settings()
app = FastAPI(debug=settings.debug)


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return settings.templates.TemplateResponse('index.jinja', {'request': request})
