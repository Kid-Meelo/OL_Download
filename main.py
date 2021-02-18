import requests
from bs4 import BeautifulSoup


# Access to website
def open_url():
    r = requests.get('https://www.onlineliga.de/login')
    soup = BeautifulSoup(r.text, "lxml")
    elements = soup.find_all(attrs={"name": "_token"})
    token = elements[0]['value']
    print(token)


if __name__ == '__main__':
    open_url()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

