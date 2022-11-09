from tech_news.database import find_news


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
    """Seu código deve vir aqui"""
