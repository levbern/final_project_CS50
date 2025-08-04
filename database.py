import sqlite3

def make_tables():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Likes (
            like_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            author TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sessions (
            session_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            expires DATETIME NOT NULL,
            FOREIGN KEY(user_id) REFERENCES User(user_id)
        );
    """)
    conn.commit()
    conn.close()


def get_users_password(username: str) -> str:
        """ Returns a hash password from a database """
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM User WHERE username = ?", (username,))
        result = cursor.fetchone()
        return result[0] if result else None


def get_user_id(username: str) -> int:
        """ Returns the user ID from the database """
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM User WHERE username = ?", (username,))
        result = cursor.fetchone()
        return result[0] if result else None


def add_user(username: str, hashed_password: str):
    """ Adds the user to the database """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO User (username, password) VALUES (?, ?)",
        (username, hashed_password)
    )
    conn.commit()
    conn.close()


def save_session(session_token: str, user_id: int):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Sessions (session_id, user_id, expires)
            VALUES (?, ?, datetime('now', '+1 hour'))
        """, (session_token, user_id))
        conn.commit()


def get_user_by_token(token: str):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.* FROM User u
            JOIN Sessions s ON u.user_id = s.user_id
            WHERE s.session_id = ? AND s.expires > datetime('now')
        """, (token,))
        return cursor.fetchone()


def add_user_like(username: str, title: str, genre: str, author: str):
    user_id = get_user_id(username)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Likes (user_id, title, genre, author) VALUES (?, ?, ?, ?)",
        (user_id, title, genre, author)
    )
    conn.commit()
    conn.close()


def delete_user_like(username: str, title: str, genre: str, author: str):
    user_id = get_user_id(username)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Likes WHERE user_id = ? AND title = ? AND genre = ? AND author = ?",
        (user_id, title, genre, author)
    )
    conn.commit()
    conn.close()


def get_likes_by_genre(genre, username) -> list:
    user_id = get_user_id(username)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM Likes WHERE user_id = ? AND genre = ?", (user_id, genre))
    data = cursor.fetchall()
    result = []
    for el in data:
        result.append(el[0])

    return result if result else []


def get_user_likes(username: str):
    user_id = get_user_id(username)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, genre FROM Likes WHERE user_id = ?", (user_id,))
    data = cursor.fetchall()
    result = []
    for el in data:
        book_info = {}
        book_info["title"] = el[0]
        book_info["authors"] = el[1]
        book_info["genre"] = el[2]
        result.append(book_info)

    return result if result else None


def delete_session(token: str):
    with sqlite3.connect('database.db') as conn:
        conn.execute("DELETE FROM Sessions WHERE session_id = ?", (token,))