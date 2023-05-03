from bs4 import BeautifulSoup
import requests

def pars(item):
   # item = input("Ссылка:\n")

    url1 = f'https://mvmonitor.ru/template/view_product_mvideo.php?sku={item}'
    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64'}


    def price(url, headers):
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, "html.parser")
            # print(soup)
            parsed_text = soup.findAll('h5', class_='text-white mb-0')
            # print(parsed_text)
            res = str(parsed_text[0])
            try:
                res = res.replace('<h5 class="text-white mb-0" itemprop="price">','')
                res = res.replace(' <i class="fas fa-ruble-sign"></i></h5>','')
                return res
            except:
                print("not found")
                return
        else:
            print("out of connection")


    print(price(url1, headers1))
