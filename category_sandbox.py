import requests
import json

category_title = str(input('Enter a category: '))

url = 'https://en.wikipedia.org/w/api.php'
params = {
    'action': 'query',
    'list': 'categorymembers',
    'cmlimit': 'max',
    'cmprop': 'title|type',
    'cmtype': 'page|subcat',
    # 'cmtitle': f'Category:{category_title}',
    'format': 'json',
    # 'cmnamespace': 14,
}

def get_category_members(category):
    params['cmtitle'] = f'Category:{category}'
    data = {}
    category_members = []

    while True:
        response = requests.get(url, params=params)
        # print(response.url)
        
        if response.status_code == 200:
            data = json.loads(response.text)
            category_members += data['query']['categorymembers']
            
            if 'continue' in data:
                params['cmcontinue'] = data['continue']['cmcontinue']
            else:
                return category_members
        else:
            print('Error: Request failed with status code', response.status_code)
            break

category_members = get_category_members(category_title)

count = 0
for member in category_members:
    if member['type'] == 'page':
        print(member['title'])
        count += 1
print(f'{count} category members in {category_title}')
