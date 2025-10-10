import threading
import time
from bs4 import BeautifulSoup
from typing import Optional
import requests
from multiprocessing import Process

A = 0

def parse(soup: BeautifulSoup) -> Optional[dict]:
    try:
        selectors = {
            'title': {'class_': ['product-card__title title-sm']},
            'brand': {'class_': ['product-card__prod-value']},
            'country': {'class_': ['product-card__prod-value d-flex align-items-center gap-1 color-gray']},
            'article': {'class_': ['product-card__articul-value color-gray']},
        }

        title_elem = soup.find(**selectors['title'])
        brand_elem = soup.find(**selectors['brand'])
        country_elem = soup.find(**selectors['country'])
        article_elem = soup.find(**selectors['article'])

        if not all([title_elem, brand_elem, country_elem, article_elem]):
            print("Не все обязательные элементы найдены на странице")
            return None

        data = {
            'title': title_elem.get_text(strip=True) if title_elem else '',
            'brand': brand_elem.get_text(strip=True) if brand_elem else '',
            'country': country_elem.get_text(strip=True) if country_elem else '',
            'article': article_elem.get_text(strip=True) if article_elem else '',
            'meta_title': f'Купить {title_elem.get_text(strip=True)} | Dental First' if title_elem else '',
            'meta_description': f'{title_elem.get_text(strip=True)} в интернет-магазине Dental First. Каталог включает '
                                f'стоматологические товары в широком диапазоне цен. Помощь специалистов, быстрая '
                                f'доставка по всей России.| Dental First' if title_elem else ''
        }
        return data
    except Exception as e:
        print(f'Возникла ошибка: {e}')
def y_test_parse(x):
    print(f'Выполняется поток: {x}')
    # time.sleep(100)
    print(f'Конец работы потока: {x}')

def one_thr(x):
    a=0
    for i in range(x):
        a += 1
        url = 'https://dental-first.ru/catalog/koronkosnimatel-ruchnoy-dvustoronniy/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # base_data = parse(soup)
    print(f'Основной поток {x} звершился\n'
          f'Выполнено {a} итераций')

def _test_parse(x):
    a=0
    for i in range(x, x+3):
        a += 1
        url = 'https://dental-first.ru/catalog/koronkosnimatel-ruchnoy-dvustoronniy/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # base_data = parse(soup)

    print(f'поток {x} звершился\n'
          f'Выполнено {a} итераций')

start = time.time()
print('начало')
t_1 = threading.Thread(target=_test_parse, args=(1,))
t_2 = threading.Thread(target=_test_parse, args=(2,))
t_32 = threading.Thread(target=_test_parse, args=(3,))
t_33 = threading.Thread(target=_test_parse, args=(3,))

t_1.start()
t_2.start()
t_32.start()
t_33.start()

t_1.join()
t_2.join()
t_32.join()
t_33.join()
# one_thr(9)

print(f'затарченное время: {time.time() - start}')