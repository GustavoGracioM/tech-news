import requests
import time


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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
