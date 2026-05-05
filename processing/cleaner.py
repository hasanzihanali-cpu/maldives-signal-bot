import re

def clean_text(text):
    text = re.sub('<.*?>', '', text)
    text = re.sub('\s+', ' ', text)
    return text.strip()
