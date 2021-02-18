import getpass

import requests
from bs4 import BeautifulSoup


# Access to website
def open_url(session: requests.Session):
    # request in the session
    r = session.get('https://www.onlineliga.de/login')
    soup = BeautifulSoup(r.text, "lxml")
    elements = soup.find_all(attrs={"name": "_token"})
    token = elements[0]['value']
    return token


def login(session: requests.Session, token: str):
    g = session.post("https://www.onlineliga.de/login",
                     params={"_token": {token},
                             "login": input("Whats your Username?"),
                             "password": getpass.getpass("Whats your Password?")})


def logintest(session: requests.Session):
    x = session.get('https://www.onlineliga.de/office/finance')
    print(x.text)
    # if  x.text = finance then return true
    # if x.text = login then return false


if __name__ == '__main__':
    # open session
    s = requests.Session()
    t = open_url(s)
    print(t)
    login(s, t)