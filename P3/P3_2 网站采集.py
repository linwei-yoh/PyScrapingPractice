#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

# 页面set 去重
pages = set()

# 此方法采用了递归 python对递归有数量限制记得是1000 小心使用
def getLinks(pageUrl):
    global pages
    r = requests.get(pageUrl)
    bsObj = BeautifulSoup(r.text)
    for link in bsObj.find_all("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 新页面被找到
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")