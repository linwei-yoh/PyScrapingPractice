#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


# 请求根据具体的表单设定字段，这里只设置了2个

def changeheaders():
    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/49.0.2623.112 "
                             "Safari/537.36",
               "Accept": "*/*"}
    url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
    req = session.get(url, headers=headers)
    bsObj = BeautifulSoup(req.text, 'lxml')
    print(bsObj.find("table", {"class": "table-striped"}).get_text)


if __name__ == '__main__':
    changeheaders()
