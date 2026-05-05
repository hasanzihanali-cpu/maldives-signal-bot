KEYWORDS = ["tax", "economy", "tourism", "policy", "fuel", "import", "inflation"]

def score_article(article):
    score = 0
    text = (article["title"] + " " + article["content"]).lower()

    for kw in KEYWORDS:
        if kw in text:
            score += 10

    if "government" in text:
        score += 10

    if len(text) > 300:
        score += 10

    category = "Society"
    if "tourism" in text:
        category = "Tourism"
    elif "economy" in text or "tax" in text:
        category = "Economy"
    elif "government" in text:
        category = "Politics"

    importance = "Low"
    if score > 70:
        importance = "High"
    elif score > 40:
        importance = "Medium"

    return {
        "score": score,
        "category": category,
        "importance": importance
    }
