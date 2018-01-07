try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import urllib3
import logging
from flask import Markup

user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
http = urllib3.PoolManager(10, headers=user_agent)

def extract_forecasts(soup, max_count):
    divs = soup.findAll(class_= 'tombstone-container')
    txt = ''

    count = 0
    for div in divs:
        div.find()
        txt = txt + str(div) + '<br />'
        count = count + 1
        if count > max_count - 1:
            break
    return Markup(txt)    

def get_web_forecast(url):

    response = http.request('GET', url)

    if not response.status is 200:
        logging.warning('not 200')
        return soup.get_text()
    soup = BeautifulSoup(response.data, "html.parser")
    
    return extract_forecasts(soup, 3)
    


def test_file():
    with open('temp.txt', 'r') as file_object:
        logging.warning('opened file')
        text = file_object.read()
        soup = BeautifulSoup(text, "html.parser")
        return extract_forecasts(soup, 3)

