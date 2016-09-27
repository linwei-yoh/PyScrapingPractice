#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

ObjUrl = 'http://pythonscraping.com/pages/itsatrap.html'

def selenium_test():
    driver = webdriver.PhantomJS(executable_path="G:/python/phantomjs-2.1.1-windows/bin/phantomjs")#设置PhantomJS路径
    driver.get(ObjUrl)
    links = driver.find_elements_by_tag_name("a")
    for link in links:
        if not link.is_displayed:
            print("The link " + link.get_attribute("href")+" is a trap")
         
    fields = driver.find_elements_by_tag_name("input")
    for field in fields:
        if not field.is_displayed():
            print("Do not change value of "+field.get_attribute("name"))
            
if __name__ == '__main__':
    selenium_test()