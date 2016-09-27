#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的标准库urllib 提供了绝大多数HTTP功能，但API差劲，效率糟糕。
# Request库是更优秀的第三方库，可以处理更复杂的HTTP请求，cookie,header等

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
 

ObjUrl = 'http://pythonscraping.com/pages/itsatrap.html'
ObjUrltest = "http://1.com/home.html"

def httpwithurllib():
    html = urlopen(ObjUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    print(bsObj)


def httpwithrequest():
    try:
        r = requests.get(ObjUrl)
    except requests.RequestException as e:
        print(e)
    else:
        bsObj = BeautifulSoup(r.text, 'lxml')
        print(bsObj)


if __name__ == '__main__':
    httpwithrequest()
