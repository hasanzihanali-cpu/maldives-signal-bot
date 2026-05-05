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

def article_exists(url):
    cursor.execute("SELECT 1 FROM articles WHERE url=?", (url,))
    return cursor.fetchone() is not None

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
    except:
        pass
