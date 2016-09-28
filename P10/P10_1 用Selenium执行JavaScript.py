#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium的选择器查找方式和BeautifulSoup不同，更直接

objUrl = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
driver = webdriver.PhantomJS(executable_path="G:/python/phantomjs/bin/phantomjs")


def javascript_test1():
    driver.get(objUrl)
    time.sleep(3)
    print(driver.find_element_by_id('content').text)
    driver.close()


def seleniumToBeautifulSoup():
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource)
    print(bsObj.find(id="content").get_text())
    

def javascript_test2():
    driver.get(objUrl)
    try:
        element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"loadedButton")))
    finally:
        print(driver.find_element_by_id("content").text)
        driver.close()

if __name__ == '__main__':
    javascript_test2()
