import requests

i = ["style.css", "style2.css"]
prox = {
    "http": "http://51.161.27.96:80",
    "https": "https://5.181.171.134:8085"
}


def main():
    for n in range(len(i)):
        page = requests.get("https://www.ucoz.ru/ucoz/v3/css/" + i[n], proxies=prox)
        print(page.status_code)


if __name__ == "__main__":
    main()