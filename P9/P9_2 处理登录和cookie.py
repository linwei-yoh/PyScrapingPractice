#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

ObjLoginUrl = "http://pythonscraping.com/pages/cookies/welcome.php"
ObjProUrl = "http://pythonscraping.com/pages/cookies/profile.php"
ObjAuthUrl = "http://pythonscraping.com/pages/auth/login.php"
params = {'username': 'AL', 'password': 'password'}


def requestwithcookie():
    r = requests.post(ObjLoginUrl, params)
    print("Cookie is set to:")
    print(r.cookies.get_dict())
    print("--------------------")
    print("Going to profile page..")
    r = requests.get(ObjProUrl, cookies=r.cookies)
    print(r.text)


def sessionwithcookie():
    session = requests.Session()
    s = session.post(ObjLoginUrl, params)
    print("Cookie is set to:")
    print(s.cookies.get_dict())
    print("--------------------")
    print("Going to profile page..")
    s = session.get(ObjProUrl)
    print(s.text)


# Http基本接入认证
def base_access_auth():
    auth = HTTPBasicAuth('AL', 'password')
    r = requests.post(ObjAuthUrl, auth=auth)
    print(r.text)


if __name__ == '__main__':
    requestwithcookie()
