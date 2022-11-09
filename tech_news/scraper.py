import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url: str):
    try:
        for _ in range(10):
            response = requests.get(
                url, timeout=3, headers={"user-agent": "Fake user-agent"}
            )
            html = response.text if response.status_code == 200 else None
            time.sleep(1)
            return html
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(".cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    title_with_space = selector.css(".entry-title::text").get()
    list_paragraph = selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()
    news = {
        "url": selector.css("link[rel~='canonical']::attr(href)").get(),
        "title": "".join(title_with_space).strip(),
        "timestamp": selector.css(".meta-date::text").get().strip(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()),
        "summary": "".join(list_paragraph).strip(),
        "category": selector.css(".category-style .label::text").get(),
        "tags": selector.css(".post-tags ul li a::text").getall(),
    }
    return news


# Requisito 5
def get_tech_news(amount):
    news = []
    html_content = fetch("https://blog.betrybe.com")
    next_page = scrape_next_page_link(html_content)
    while next_page and len(news) < int(amount):
        for link in scrape_novidades(html_content):
            if len(news) < int(amount):
                news_detail = fetch(link)
                news.append(scrape_noticia(news_detail))
        html_content = fetch(next_page)
        next_page = scrape_next_page_link(html_content)
    create_news(news)
    return news
