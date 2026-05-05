import feedparser
from config.settings import RSS_FEEDS

def fetch_articles():
    articles = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title", ""),
                "content": entry.get("summary", ""),
                "url": entry.get("link", ""),
                "source": feed_url
            })

    return articles
