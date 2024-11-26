import importlib.resources

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

import uvicorn

with importlib.resources.path("quizmaster", "templates") as templates_path:
    templates = Jinja2Templates(directory=templates_path)


async def index(request):
    return templates.TemplateResponse(request, "index.html")


routes = [
    Route("/", endpoint=index),
    Mount("/static", StaticFiles(packages=["quizmaster"]), name="static"),
]

app = Starlette(debug=True, routes=routes)


async def start(host: str, port: int):
    config = uvicorn.Config(app=app, host=host, port=port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()
