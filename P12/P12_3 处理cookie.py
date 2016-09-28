#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver


def getcookiefromweb(url):
    driver = webdriver.PhantomJS(executable_path="G:/python/phantomjs/bin/phantomjs")
    driver.get(url)
    driver.implicitly_wait(1)
    print(driver.get_cookies())


if __name__ == '__main__':
    getcookiefromweb("http://www.baidu.com")