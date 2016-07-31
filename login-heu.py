#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import os
import sys
import random
import cookielib
import requests
from bs4 import BeautifulSoup


requests = requests.Session()
requests.cookies = cookielib.LWPCookieJar('cookies')
try:
    requests.cookies.load(ignore_discard=True)
except:
    pass


def download_captcha():
    url="http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS"
    r=requests.get(url)
    with open('captcha.jpg','wb') as image:
        image.write(r.content)


def build_form():
    username='2013084125'
    password='1995927'
    download_captcha()

    os.system('xdg-open {}'.format('captcha.jpg'))
    captcha_code=raw_input(u'please enter the code:')

    url="http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS?mode=4"

    headers={
    'Accept':'image/webp,image/*,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    form={
    'WebUserNO':username,
    'Password':password,
    'Agnomen':captcha_code,
    'submit.x':random.randint(1,100),
    'submit.y':random.randint(1,100)
    }

    r=requests.post(url,headers=headers,data=form)
    
    if not r.headers['Content-Type'].endswith('GBK'):
        print u'Login success'
    else:
        print u'Login error'
    requests.cookies.save()
    print r.status_code

    year_term_no=21 # from bottom to end,2012-2013 第一学年

    base_url="http://jw.hrbeu.edu.cn/ACTIONQUERYELECTIVERESULTBYSTUDENT.APPPROCESS"

    r=requests.get(base_url)
    
    with open('temp.html','w+') as t:
        t.write(r.content)
    base_soup=BeautifulSoup(r.content,"lxml")

    student_name=base_soup.find('td').get_text()
    print student_name

def get_schedule():
    
    pass



if __name__=='__main__':

    build_form()