import getpass

import requests
from bs4 import BeautifulSoup

season_10 = "https://www.onlineliga.de/team/overview/history/season?userId=47895&season=10"


# Access to website
def get_ol_token(session: requests.Session):
    # request in the session
    response = session.get('https://www.onlineliga.de/login')
    soup = BeautifulSoup(response.text, "lxml")
    elements = soup.find_all(attrs={"name": "_token"})
    token = elements[0]['value']
    return token


def login(session: requests.Session, token: str):
    login_response = session.post("https://www.onlineliga.de/login",
                                  params={"_token": {token},
                                          "login": input("Whats your Username?"),
                                          "password": getpass.getpass("Whats your Password?")})
    check_login(login_response)


def check_login(response: requests.Response):
    # if not response.text:
    #     print("login successful")
    if len(response.text) == 0:
        print("login successful")
    else:
        print("login unsuccessful")


def get_matchlineup(session: requests.Session):
    match_url = "https://www.onlineliga.de/match/lineup?season=10&matchId=90581"
    match_response = session.get(match_url)

# x[:-2]
# 'Hello Worl'


def get_seasons_played(session: requests.Session):
    history_url = "https://www.onlineliga.de/team/overview/history?userId=47895"


def get_ol_userid(session: requests.Session):
    landing_url = "https://www.onlineliga.de/"
    response = session.get(landing_url)
    soup = BeautifulSoup(response.text, "lxml")
    elements = soup.find_all(lambda t: t.get("onclick").startswith("olAnchorNavigation.load('/team/squad'"))
    user_id = elements[0]['value']



# def logintest(session: requests.Session):
#     x = session.get('https://www.onlineliga.de/office/finance')
#     print(x.text)
# if  x.text = finance then return true
# if x.text = login then return false


if __name__ == '__main__':
    # open session
    ol_session = requests.Session()
    ol_token = get_ol_token(ol_session)
    print(ol_token)
    login(ol_session, ol_token)
    get_ol_userid(ol_session)