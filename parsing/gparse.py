import requests, json
from bs4 import BeautifulSoup


query = input('Search: ')
query = query.replace(' ', '+')
url = URL = f"https://google.com/search?q={query}"
USER_AGENT = "Mozilla/5.0 (Macintosh;"
            " Intel Mac OS X 10.14; rv:65.0)"
            " Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}
snew_class = 'kvH3mc'  # edit if don't work

page = requests.get(url, headers=headers)


def search_results(soup, cls):
    results = []
    for g in soup.find_all('div', class_=cls):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
    return results


if page.status_code == 200:
    soup = BeautifulSoup(page.content, "lxml")
    res = search_results(soup, snew_class)
    print(res)

    with open(f"data/{query}_go.json", "w") as write_file:
        json.dump(res, write_file)
