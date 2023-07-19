from bs4 import BeautifulSoup

soup = BeautifulSoup(open("data//nax_page.html").read())

content = soup.find("div", class_="front_goods")
content.find_all("div")

# ...
