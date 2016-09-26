#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests

'''P9.1 提交一个基本表单'''

'''处理表单的地址 可以再chrome中F12到调试界面，
选择network标签,点击登录,观察network下提交地址与提交方式'''

params = {'firstname':'AL','lastname':'Lin'}
r = requests.post("http://pythonscraping.com/pages/files/processing.php",data=params)
print(r.text)