# final CS50 project
Harvard CS50 Introduction to Computer Science final project

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenLibrary](https://img.shields.io/badge/OpenLibrary-FFC107?logo=openlibrary&logoColor=black)](https://openlibrary.org/)

**Видеопрезентация проекта**: [Ссылка на видео](ВАША_ССЫЛКА_НА_ВИДЕО) (замените на актуальный URL)

## 🚀 О проекте
Интеллектуальная платформа для книголюбов, позволяющая:
- 🔍 Искать книги по жанру через интеграцию с OpenLibrary
- ❤️ Сохранять понравившиеся книги в персональную коллекцию
- 📚 Просматривать историю лайков в удобном интерфейсе

## ⚙️ Установка и запуск

### Требования
- Python 3.8+
- Активное интернет-соединение

```bash
# Клонировать репозиторий
git clone https://github.com/ваш-username/BookFinder.git
cd BookFinder

# Настройка виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (Linux/macOS)
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск сервера
uvicorn main:app --reload