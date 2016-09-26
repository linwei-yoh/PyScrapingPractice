#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,'lxml')

# find 是 findAll(limit = 1)时候的特例 即查找第一个符合条件的
# 输出符合要求的第一个标签，将次级标签作为child 逐个输出
count = 0
for child in bsObj.find("table",{"id":"giftList"}).children:
    print("child:" + str(count))
    print(child)
    count += 1

print("--------------------------------------------------------------")
#找到table标签的第一个tr标签，用next_sibling显示它所有的兄弟标签，不显示他本身
count = 0
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print("child:" + str(count))
    print(sibling)
    count += 1

print("--------------------------------------------------------------")