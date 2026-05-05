from ingestion.rss_fetcher import fetch_articles
from processing.cleaner import clean_text
from processing.scorer import score_article
from storage.database import article_exists, save_article
from ai.summarizer import summarize
from delivery.telegram_bot import send_message
from config.settings import SCORE_THRESHOLD

def run_pipeline():
    articles = fetch_articles()

    for article in articles:
        if article_exists(article["url"]):
            continue

        article["content"] = clean_text(article["content"])

        score_data = score_article(article)
        article.update(score_data)

        if article["score"] < SCORE_THRESHOLD:
            continue

        summary = summarize(article)

        send_message(summary, article["url"])
        save_article(article)
