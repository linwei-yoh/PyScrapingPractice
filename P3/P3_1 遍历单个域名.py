#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


r = requests.get("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(r.text)

# 查找当前页面下 所有带有href属性的 a标签
for link in bsObj.find_all("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
