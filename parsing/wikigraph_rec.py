from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()  # создаём объект графа
nodes = []
edges = []
temp_url = "https://ru.wikipedia.org"
start_url = "https://ru.wikipedia.org/wiki/Философия"

max_call = 100
my_call = 0
max_deep = 5
my_deep = 0


def path_wiki(url: str = start_url):
    global my_call, max_call, max_deep, my_deep

    soup = BeautifulSoup(requests.get(url).text, "lxml")
    texts = soup.find_all("p")

    for text in texts:
        names = text.find_all("a", href=True)
        for name in names:
            if name.text[0] != "[":
                url = temp_url + name['href']
                print(url)
                print(name.text)
                if max_call >= my_call:
                    path_wiki(url)
                max_call += 1


path_wiki(start_url)

# определяем список узлов (ID узлов)
# nodes = [1, 2, 3, 4, 5]

# определяем список рёбер
# список кортежей, каждый из которых представляет ребро
# кортеж (id_1, id_2) означает, что узлы id_1 и id_2 соединены ребром
# edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)]

# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()
