import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)

menu = """
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """

posts = [
    "Digite quantas notícias serão buscadas",
    "Digite o título:",
    "Digite a data no formato aaaa-mm-dd:",
    "Digite a tag:",
    "Digite a categoria:",
]

functions = [
    get_tech_news,
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
    top_5_news,
    top_5_categories,
]


def get_functions(menu_value):
    if int(menu_value) <= 4:
        print(posts[int(menu_value)])
        input_value = input()
        return functions[int(menu_value)](input_value)
    elif int(menu_value) >= 5 and int(menu_value) <= 6:
        return functions[int(menu_value)]()


# Requisito 12
def analyzer_menu():
    print(menu)
    menu_value = input()
    if int(menu_value) >= 0 and int(menu_value) <= 6:
        return get_functions(menu_value)
    elif int(menu_value) == 7:
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
