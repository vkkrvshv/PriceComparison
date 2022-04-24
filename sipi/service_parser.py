import requests
from link import final_link
from bs4 import BeautifulSoup


def get_html(url, params=None):
    """
    Функция получения ссылки сайта аптеки

    :param url: ссылка сайта аптеки
    :param params: параметры (default: None)
    :return: r -- GET-запрос на получение ссылки
    """
    r = requests.get(url, headers=HEADERS,
                     params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html,
                         'html.parser')
    print(soup)
    pagination = soup.find_all(med_list["pagination_prefix"], class_=med_list["pagination"])
    if pagination:
        return int(pagination[-2].get_text())
    else:
        return 1


def get_content(html):
    """
    Функция получения контента сайта аптеки

    :param html: ссылка страницы сайта аптеки
    :return: medicines[] -- список лекарств аптеки
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(med_list["item_prefix"], class_=med_list["item_class"])
    medicines = []
    for item in items:
        medicines.append({
            'title': item.find(med_list["title_prefix"], class_=med_list["title_class"]).get_text(strip=True),
            'link': med_list["HOST"] + item.find(med_list["link_prefix"], class_=med_list["link_class"]).get(
                med_list["get_in_link"]),
            'price': item.find(med_list["price_prefix"], class_=med_list["price_class"]).get_text(strip=True)
        }
        )
    return medicines


def parse():
    """
    Функция парсинга с сайта указанного товара

    :return: medicines[] -- список лекарств аптеки, а в случае ошибки - вывод error
    """
    html = get_html(URL)
    if html.status_code != 0:
        medicines = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(
                f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params={'': page})
            medicines.extend(get_content(html.text))
        print(medicines)
    else:
        print('ERROR')


if __name__ == '__main__':
    a = int(input())
    URL = final_link(str(input()))[a]
    print(URL)
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
               'accept': '*/*'}

    match a:  # match-case a
        case 0:  # если равен 0
            med_list = {"HOST": 'https://366.ru',
                        "pagination": "b-pagination__item",
                        "pagination_prefix": "a",
                        "item_class": "listing_product",
                        "item_prefix": "div",
                        "title_class": "listing_product__title",
                        "title_prefix": "a",
                        "link_class": "listing_product__title",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "price",
                        "price_prefix": "span"
                        }
        case 1:  # если равен 1
            med_list = {"HOST": 'https://planetazdorovo.ru',
                        "pagination": "pagination__item",
                        "pagination_prefix": "span",
                        "item_class": "card-list__element",
                        "item_prefix": "div",
                        "title_class": "product-card__title",
                        "title_prefix": "div",
                        "link_class": "product-card__title",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "product-card__price ",
                        "price_prefix": "div"
                        }
        case 2:  # если равен 2
            med_list = {"HOST": 'https://gorzdrav.org',
                        "pagination": "b-pagination__item",
                        "pagination_prefix": "a",
                        "item_class": "c-prod-item",
                        "item_prefix": "div",
                        "title_class": "c-prod-item__title",
                        "title_prefix": "div",
                        "link_class": "c-prod-item__link",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "b-price",
                        "price_prefix": "span"
                        }
        case 3:  # если равен 3
            med_list = {"HOST": 'https://budzdorov.ru',
                        "pagination": "catalog-toolbar-pages__item",
                        "pagination_prefix": "div",
                        "item_class": "product-list-mode-grid__item",
                        "item_prefix": "div",
                        "title_class": "product__title_highlight",
                        "title_prefix": "span",
                        "link_class": "product__title",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "product__active-price",
                        "price_prefix": "div"
                        }
        case 4:  # если равен 4
            med_list = {"HOST": 'https://stolichki.ru',
                        "pagination": "paging-list__link",
                        "pagination_prefix": "a",
                        "item_class": "col-12-class",
                        "item_prefix": "div",
                        "title_class": "text-black-class",
                        "title_prefix": "a",
                        "link_class": "text-black-class",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "product-price",
                        "price_prefix": "p"
                        }
        case 5:  # если равен 5
            med_list = {"HOST": 'https://www.rigla.ru',
                        "pagination": "catalog-toolbar-pages__item",
                        "pagination_prefix": "div",
                        "item_class": "product-list-mode-grid__item",
                        "item_prefix": "div",
                        "title_class": "product__title",
                        "title_prefix": "a",
                        "link_class": "product__title",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "product__active-price-number",
                        "price_prefix": "span"
                        }
        case 6:  # если равен 6
            med_list = {"HOST": 'https://zdravcity.ru',
                        "pagination": "sc-3631d8cd-0",
                        "pagination_prefix": "a",
                        "item_class": "sc-3a08f6ad-2",
                        "item_prefix": "div",
                        "title_class": "sc-3a08f6ad-6",
                        "title_prefix": "a",
                        "link_class": "sc-3a08f6ad-6",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "sc-3af8b63b-0",
                        "price_prefix": "div"
                        }
        case 7:  # если равен 7
            med_list = {"HOST": 'https://www.asna.ru',
                        "pagination": "",
                        "pagination_prefix": "a",
                        "item_class": "product_product__ZvoP0",
                        "item_prefix": "div",
                        "title_class": "product_name__VzTPG",
                        "title_prefix": "a",
                        "link_class": "product_name__VzTPG",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "catalogPrice_price__TRAFl",
                        "price_prefix": "span"
                        }
        case 8:  # если равен 8
            med_list = {"HOST": 'https://www.eapteka.ru',
                        "pagination": "custom-pagination__item",
                        "pagination_prefix": "a",
                        "item_class": "cc-item ",
                        "item_prefix": "section",
                        "title_class": "cc-item--title",
                        "title_prefix": "a",
                        "link_class": "cc-item--title",
                        "link_prefix": "a",
                        "get_in_link": "href",
                        "price_class": "price--num",
                        "price_prefix": "span"
                        }

    # HOST = 'https://366.ru'

    parse()

    print(get_html(URL))
