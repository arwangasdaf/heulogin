#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException  
#引入ActionChains鼠标操作类  
from selenium.webdriver.common.action_chains import ActionChains 
import time


driver = webdriver.PhantomJS()

driver.get("http://flights.ctrip.com/booking/SHA-CAN-day-1.html?DDate1=2017-10-29")
#target = driver.find_element_by_class_name("data_travelsky")
#driver.execute_script("arguments[0].scrollIntoView();", target)
#time.sleep(15)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,20000)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,30000)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,40000)")
time.sleep(5)

pageSource = driver.page_source
html_parse = BeautifulSoup(pageSource , "lxml")
#拿到所有的航班的div
temp = html_parse.findAll("div","search_box_light")
for div in temp:
    company  = div.find("strong" , "flight_logo").get_text()
    hangban = div.find("div" , "J_flight_no").find("span").get_text()
    start_time = div.find("td" , "right").find("strong" , "time").get_text() 
    end_time =  div.find("td" , "left").find("strong" , "time").get_text()
    
    jixing = div.find("div" , "J_flight_no").find("span").find_next("span").get_text()
    
    start_airport = div.find("td" , "right").find("strong" , "time").find_next("div").get_text()
    end_airport  =  div.find("td" , "left").find("strong" , "time").find_next("div").get_text()
    #zhundianlv = div.find("span" , "J_punctuality").get_text()
    
    price = div.find("span","base_price02").get_text()
    if jixing == u"共享":
        print("filter----"+ jixing)
    else:
        print(hangban)  
     


