# final CS50 project
Harvard CS50 Introduction to Computer Science final project

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenLibrary](https://img.shields.io/badge/OpenLibrary-FFC107?logo=openlibrary&logoColor=black)](https://openlibrary.org/)

**Video Demo**: [Project Presentation](YOUR_VIDEO_URL) (replace with actual URL)

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
git clone https://github.com/your-username/BookFinder.git
cd BookFinder

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
| ❤️ **Personal Library** | Persistent like system with local JSON storage                                 | Session-based authentication           |
| 📱 **Responsive Design** | Mobile-first interface with adaptive layouts                                   | CSS Grid/Flexbox                        |
| ⚡ **API Optimization** | Cached requests and batch processing for faster response times                | Redis caching layer                    |

</div>


# 🛠 Tech Stack

<div align="center">

| **Component**          | **Technology**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
|  backend  | FastAPI               |
| Frontend | Jinja2 Templates                                 |
| API integration | OpenLibrary                                   |
| Authentication | Session Cookies                |

</div>
