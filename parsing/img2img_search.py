from pathlib import Path
import json
import os
import requests


path = "data\\image"
paths = [str(f.absolute()) for f in Path(path).rglob("*")]
print(paths)
for file_path in paths:
    search_url = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(file_path, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(search_url, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = search_url + '?' + query_string

    print(img_search_url)
    os.system('start "' + img_search_url + '"')
