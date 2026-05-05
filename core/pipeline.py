from ingestion.rss_fetcher import fetch_articles
from processing.cleaner import clean_text
from processing.scorer import score_article
from processing.deduplicator import is_duplicate
from storage.database import article_exists, save_article, get_recent_titles
from ai.summarizer import summarize
from delivery.telegram_bot import send_message
from config.settings import SCORE_THRESHOLD

def run_pipeline():
    articles = fetch_articles()

    if not articles:
        print("[PIPELINE] No articles fetched.")
        return

    recent_titles = get_recent_titles()

    for article in articles:

        # skip if exact URL already seen
        if article_exists(article["url"]):
            continue

        # skip if fuzzy duplicate title
        if is_duplicate(article, recent_titles):
            print(f"[PIPELINE] Duplicate skipped: {article['title']}")
            continue

        # clean content
        article["content"] = clean_text(article["content"])

        # score and categorize
        score_data = score_article(article)
        article.update(score_data)

        # skip low scoring articles
        if article["score"] < SCORE_THRESHOLD:
            continue

        # summarize with AI
        summary = summarize(article)

        if summary is None:
            print(f"[PIPELINE] Summarization failed, skipping: {article['title']}")
            continue

        # deliver to Telegram
        send_message(summary, article["url"])

        # save to database
        save_article(article)

        print(f"[PIPELINE] Sent: {article['title']} (score: {article['score']})")
