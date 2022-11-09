from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news = sorted(
        find_news(), key=lambda d: (-d["comments_count"], d["title"])
    )
    list_order = [n for n in news if news.index(n) < 5]
    list_news = [(n["title"], n["url"]) for n in list_order]
    return list_news


# Requisito 11
def top_5_categories():
    news = Counter([n["category"] for n in find_news()])
    list_order = [
        key for key, n in sorted(news.items(), key=lambda d: (-d[1], d[0]))
    ]
    return list_order
