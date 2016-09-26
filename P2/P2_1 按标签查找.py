#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

#find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs):
#recursive True遍历子标签 False 只查一级标签

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,'lxml')

# 含有指定属性的 标签
nameList = bsObj.findAll("span",{"class":"green"}) #（"",{"class":"green"}）所有含有"class":"green"属性的标签
for name in nameList:
    # print(name)
    # get_text()ba HTML文档中所有的标签都清楚（超链接，段落，标签），返回只包含文字的字符串
    print(name.get_text())

#文本内容匹配
nameList = bsObj.findAll(text="the prince")
print(len(nameList))

#keyword 选择具有指定属性的标签  这是个冗余功能 不推荐
# alltext = bsObj.findAll(id = "text") #查找含有 id = "text"的标签
# print(alltext[0])
