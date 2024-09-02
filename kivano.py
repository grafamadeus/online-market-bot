from bs4 import BeautifulSoup as Bs
import requests


pics = {'kompyutery': [], 'krasota-i-zdorove': [], 'elektronika': []}
results = {'kompyutery': [], 'krasota-i-zdorove': [], 'elektronika': []}

def kivano(url):
    r = requests.get(f'https://www.kivano.kg/{url}')
    soup = Bs(r.text, 'html.parser')
    items = soup.find_all('div', class_='item product_listbox oh')

    category = url  
    new_list = []

    for i in items:
        new_list.append({
            'image': i.find('div', class_='listbox_img pull-left').find('a').find('img').get('src'),
            'title': i.find('div', class_='pull-right rel').find('div', class_='product_text pull-left').find('div', class_='listbox_title oh').find('strong').find('a').get_text(strip=True),
            'Цена': i.find('div', class_='pull-right rel').find('div', class_='motive_box pull-right').find('div', class_='listbox_price text-center').find('strong').get_text(strip=True),
            'Артикул': i.get('data-key')
        })

   
    pics[category] = [item['image'] for item in new_list]
    results[category] = [
        '\n\n'.join(f"{key}: {value}" for key, value in item.items() if key != 'image')
        for item in new_list
    ]

    return results[category]


result = kivano('kompyutery')
result2 = kivano('krasota-i-zdorove')
result3 = kivano('elektronika')


def create_generator(data_type):
    for item in pics[data_type]:
        yield item

def create_result_generator(data_type):
    for item in results[data_type]:
        yield item

callpic = create_generator('kompyutery')
callpic2 = create_generator('krasota-i-zdorove')
callpic3 = create_generator('elektronika')

callres = create_result_generator('kompyutery')
callres2 = create_result_generator('krasota-i-zdorove')
callres3 = create_result_generator('elektronika')
