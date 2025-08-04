"""Book Recommendation System with Authentication"""
import secrets
from typing import Optional

from fastapi import (
    FastAPI, 
    Request, 
    HTTPException, 
    Form, 
    status, 
    Body, 
    Depends
)
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext

from init import cmc_client
import database

# ---------- Configuration ---------- #
app = FastAPI(title="Book Recommender", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
database.make_tables()

# Security configuration
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
SESSION_COOKIE = "session_token"
TOKEN_BYTES = 32

# ---------- Helper Functions ---------- #
def get_current_user(request: Request) -> Optional[str]:
    """Retrieve authenticated user from session cookie"""
    if token := request.cookies.get(SESSION_COOKIE):
        if user := database.get_user_by_token(token):
            return user[1]
    return None

def template_response(
    request: Request, 
    template: str, 
    context: dict = None, 
    status_code: int = 200
) -> HTMLResponse:
    """Create standardized template response with user context"""
    return templates.TemplateResponse(
        template,
        {
            "request": request,
            "current_user": get_current_user(request),
            **(context or {})
        },
        status_code=status_code
    )

# ---------- Authentication Routes ---------- #
@app.get("/", response_class=HTMLResponse)
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    """Landing page with personalized content"""
    return template_response(request, "home.html")

@app.get("/register", response_class=HTMLResponse)
async def registration_form(request: Request):
    """User registration form"""
    return template_response(request, "register.html", {"error": None})

@app.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    """Handle new user registration"""
    if database.get_user_id(username):
        return template_response(
            request,
            "login.html",
            {"error": "username_exists"},
            status.HTTP_401_UNAUTHORIZED
        )
    
    database.add_user(username, pwd_ctx.hash(password))
    return RedirectResponse("/home", status.HTTP_303_SEE_OTHER)

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    """User login form"""
    return template_response(request, "login.html", {"error": None})

@app.post("/login", response_class=HTMLResponse)
async def authenticate_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    """Handle user authentication"""
    stored_hash = database.get_users_password(username)
    if not stored_hash or not pwd_ctx.verify(password, stored_hash):
        return template_response(
            request,
            "login.html",
            {"error": "invalid_credentials"},
            status.HTTP_401_UNAUTHORIZED
        )

    token = secrets.token_urlsafe(TOKEN_BYTES)
    response = RedirectResponse("/home", status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key=SESSION_COOKIE,
        value=token,
        httponly=True,
        max_age=3600,
        samesite="Lax"
    )
    database.save_session(token, database.get_user_id(username))
    return response

@app.get("/logout")
async def logout():
    """Terminate user session"""
    response = RedirectResponse("/login")
    response.delete_cookie(SESSION_COOKIE)
    return response

# ---------- Book Management Routes ---------- #
@app.get("/search", response_class=HTMLResponse)
async def search_interface(request: Request, genre: str = "0"):
    """Book search interface"""
    if not get_current_user(request):
        return template_response(
            request,
            "error.html",
            {"error": "Authentication required"},
            status.HTTP_401_UNAUTHORIZED
        )
    
    return template_response(request, "search.html", {"genre": genre, "books": []})

@app.post("/search", response_class=HTMLResponse)
async def search_books(request: Request, genre: str = Form(...)):
    """Handle book search requests"""
    genre = genre.lower()

    user = get_current_user(request)
    books = await cmc_client.get_books_by_genre(genre, user)
    print(books)
    return template_response(
        request, 
        "search.html", 
        {
            "genre": genre, 
            "books": books
        }
    )

@app.post("/like")
async def add_favorite(data: dict = Body(...)):
    """Add book to user favorites"""
    database.add_user_like(
        data['login'],
        data['title'],
        data['genre'],
        data['author']
    )
    return {"status": "success"}

@app.post("/remove_like")
async def remove_favorite(data: dict = Body(...)):
    """Remove book from user favorites"""
    database.delete_user_like(
        data['login'],
        data['title'],
        data['genre'],
        data['author']
    )
    return {"status": "success"}

@app.get("/liked", response_class=HTMLResponse)
async def favorites_list(request: Request):
    """Display user's favorite books"""
    if not (user := get_current_user(request)):
        return template_response(
            request,
            "error.html",
            {"error": "Authentication required"},
            status.HTTP_401_UNAUTHORIZED
        )
    
    return template_response(
        request,
        "liked.html",
        {"books": database.get_user_likes(user)}
    )

# ---------- Error Handling ---------- #
@app.exception_handler(404)
async def not_found_handler(request: Request, _):
    """Custom 404 error page"""
    return template_response(
        request,
        "error.html",
        {"error": "Page not found"},
        status.HTTP_404_NOT_FOUND
    )
