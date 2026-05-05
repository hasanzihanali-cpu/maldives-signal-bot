import feedparser
from config.settings import RSS_FEEDS

def fetch_articles():
    articles = []

    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)

            if feed.bozo:
                print(f"[RSS WARN] Feed may have issues: {feed_url}")

            for entry in feed.entries:
                articles.append({
                    "title": entry.get("title", ""),
                    "content": entry.get("summary", ""),
                    "url": entry.get("link", ""),
                    "source": feed_url
                })

            print(f"[RSS] Fetched {len(feed.entries)} articles from {feed_url}")

        except Exception as e:
            print(f"[RSS ERROR] Failed to fetch {feed_url}: {e}")

    return articles
