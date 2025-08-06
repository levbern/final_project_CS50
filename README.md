# final CS50 project
Harvard CS50 Introduction to Computer Science final project

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenLibrary](https://img.shields.io/badge/OpenLibrary-FFC107?logo=openlibrary&logoColor=black)](https://openlibrary.org/)

**Video Demo**: [Project Presentation](YOUR_VIDEO_URL)

## 🚀 About
Intelligent platform for book lovers offering:
- 🔍 Genre-based book search via OpenLibrary API
- ❤️ Save favorite books to personal collection
- 📚 View liked books history with intuitive UI

## ⚙️ Installation

### Requirements
- Python 3.8+
- Active internet connection

```bash
# Clone repository
git clone https://github.com/levbern/final_project_CS50.git
cd final_project_CS50

# Virtual environment setup
python -m venv venv

# Activation (Windows)
venv\Scripts\activate

# Activation (Linux/macOS)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn main:app --reload

# Access via browser:
http://127.0.0.1:8000

```

## ✨ Key Features

<div align="center">
  
| **Feature**          | **Description**                                                                 | **Tech Implementation**                |
|-----------------------|---------------------------------------------------------------------------------|-----------------------------------------|
| 🔍 **Smart Search**   | 20+ popular genres supported through OpenLibrary API integration               | Advanced query parsing                 |
| ❤️ **Personal Library** | Persistent like system with local storage                                 | Session-based authentication           |

</div>


## 🛠 Tech Stack

<div align="center">

| **Component**          | **Technology**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
|  backend  | FastAPI               |
| Frontend | Jinja2 Templates                                 |
| API integration | OpenLibrary                                   |
| Authentication | Session Cookies                |

</div>

## ℹ️ Files information 
1) **static/css/styles.css** stores all the styles that I use on the site. With its help, I made my pages beautiful and easy to read. 
2) **static/img/creator.jpg** is a photo of the creator, which is transferred to the main page of the site. 
3) **templates/base.html** is the base template that all other templates inherit. It contains the header and footer, and styles are also included in it. 
4) **templates/error.html** is an error template. An error message is transferred to it if the user does something wrong.
5) **templates/home.html** — the main page template. It contains brief information about the site's capabilities, as well as an invitation to register/log in to an account.
6) **templates/liked.html** is a template for the liked books page. It contains a list of cards with information about the books you liked.
7) **templates/login.html** is a template for logging into an account, consisting of forms that request a login and password.
8) **templates/register.html** is a template for registering on the site, based on a form that requests login, password, and re-entry.
9) **templates/search.html** is a template selection, consisting of a window in which you need to enter a genre, and a "search" button. After the user has entered the genre and clicked this button, the site displays the books found in the open library by genre.
10) **database.py** is the request handler in the data resources
11) **http_client.py** is the request handler in the openlibrary API.
12) **init.py** initializes the client that makes requests to the library.
13) **main.py** is the main file of the program. All post and get requests on my site are processed there.