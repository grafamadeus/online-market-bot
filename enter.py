from bs4 import BeautifulSoup as Bs
import requests


pics = {'videokarty_bishkek': [], 'sistemy-ohlazhdeniya_bishkek': [], 'akustika_kolonki_bishkek': []}
results = {'videokarty_bishkek': [], 'sistemy-ohlazhdeniya_bishkek': [], 'akustika_kolonki_bishkek': []}

def enter(url):
    r = requests.get(f'https://www.enter.kg/{url}')
    soup = Bs(r.text, 'html.parser')
    items = soup.find_all('div', class_='product vm-col vm-col-1')

    category = url  
    new_list = []

    for i in items:
        new_list.append({
            'image': i.find('table').find('tr').find_all('td')[0].find('a', class_='product-image-link').find('img').get('src'),
            'title': i.find('table').find('tr').find_all('td')[1].find_all('div', class_='rows')[0].find('span').find('a').get_text(strip=True),
            'Цена': i.find('table').find('tr').find_all('td')[1].find_all('div', class_='rows')[1].find('table').find('tr').find_all('td')[1].find('span').get_text(strip=True),
            'Артикул': i.find('table').find('tr').find_all('td')[1].find_all('div', class_='rows')[1].find('table').find('tr').find_all('td')[2].find('span', class_='sku').find('span').get_text(strip=True)
        })

    


    pics[category] = [item['image'] for item in new_list]
    results[category] = [
        '\n\n'.join(f"{key}: {value}" for key, value in item.items() if key != 'image')
        for item in new_list
    ]

    return results[category]


result = enter('videokarty_bishkek')
result2 = enter('sistemy-ohlazhdeniya_bishkek')
result3 = enter('akustika_kolonki_bishkek')


def create_generator(data_type):
    for item in pics[data_type]:
        yield item

def create_result_generator(data_type):
    for item in results[data_type]:
        yield item

callpic4 = create_generator('videokarty_bishkek')
callpic5 = create_generator('sistemy-ohlazhdeniya_bishkek')
callpic6 = create_generator('akustika_kolonki_bishkek')

callres4 = create_result_generator('videokarty_bishkek')
callres5 = create_result_generator('sistemy-ohlazhdeniya_bishkek')
callres6 = create_result_generator('akustika_kolonki_bishkek')

