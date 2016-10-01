#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10s")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return



if __name__ == '__main__':
    driver = webdriver.PhantomJS(executable_path="G:/python/phantomjs/bin/phantomjs")
    driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
    waitForLoad(driver)
    print(driver.page_source)