from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import TEMPLATES_DIR

router = APIRouter()
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


_PAGE_TITLES = {
    "/": "CGPA 4.04",
    "/home": "Home Page",
    "/trips": "My Trips",
    "/map": "Map Page",
    "/ai": "AI Page",
    "/budget": "Budget Page",
}


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return _render_page(request, "Home.html")


@router.get("/home", response_class=HTMLResponse)
def home_page(request: Request):
    return _render_page(request, "Home.html")


@router.get("/trips", response_class=HTMLResponse)
def trips_page(request: Request):
    return _render_page(request, "trips.html")


@router.get("/map", response_class=HTMLResponse)
def map_page(request: Request):
    return _render_page(request, "map.html")


@router.get("/ai", response_class=HTMLResponse)
def ai_page(request: Request):
    return _render_page(request, "ai.html")


@router.get("/budget", response_class=HTMLResponse)
def budget_page(request: Request):
    return _render_page(request, "budget.html")


def _render_page(request: Request, template_name: str):
    title = _PAGE_TITLES.get(request.url.path, "CGPA 4.04")
    return templates.TemplateResponse(request, template_name, {"title": title})
