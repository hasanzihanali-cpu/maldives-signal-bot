import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT UNIQUE,
    title TEXT,
    content TEXT,
    source TEXT,
    score INTEGER,
    category TEXT,
    sent INTEGER DEFAULT 0
)
""")

conn.commit()


def article_exists(url):
    try:
        cursor.execute("SELECT 1 FROM articles WHERE url=?", (url,))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"[DB ERROR] article_exists failed: {e}")
        return False


def save_article(article):
    try:
        cursor.execute("""
        INSERT INTO articles (url, title, content, source, score, category, sent)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            article["url"],
            article["title"],
            article["content"],
            article["source"],
            article["score"],
            article["category"],
            1
        ))
        conn.commit()
    except Exception as e:
        print(f"[DB ERROR] Failed to save article: {e}")


def article_exists(url):
    try:
        cursor.execute("SELECT 1 FROM articles WHERE url=?", (url,))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"[DB ERROR] article_exists failed: {e}")
        return False


def get_recent_titles(limit=200):
    try:
        cursor.execute(
            "SELECT title FROM articles ORDER BY id DESC LIMIT ?", (limit,)
        )
        return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"[DB ERROR] get_recent_titles failed: {e}")
        return []
