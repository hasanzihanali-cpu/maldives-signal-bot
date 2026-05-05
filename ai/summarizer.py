from openai import OpenAI
from config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize(article):
    prompt = f"""
Summarize this news into strict format:

Headline
Summary (1-2 lines)
Why it matters
Impact

Article:
{article['content']}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"[AI ERROR] Failed to summarize article: {e}")
        return None
