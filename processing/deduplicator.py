from rapidfuzz import fuzz

def is_duplicate(new_article, existing_titles):
    for title in existing_titles:
        if fuzz.ratio(new_article["title"], title) > 90:
            return True
    return False
