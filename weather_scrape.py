try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import urllib3
import logging
from flask import Markup
import os.path
import time
import html2text

user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
http = urllib3.PoolManager(10, headers=user_agent)
weather_cache_file = 'weather_cache.txt'

def extract_forecasts(soup, max_count):
    divs = soup.findAll(class_= 'tombstone-container')
    txt = ''

    count = 0
    for div in divs:
        div.find()
        for img in div.find_all('img'):
            img_url = img['src']
            img['src'] = 'https://forecast.weather.gov/' + img_url
            img['width'] = 32
            img['height'] = 32

        div['class'] = 'day' + str(count+1)
        txt = txt + str(div)
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
    return extract_forecasts(soup, 6)

def test_file():
    with open('temp.txt', 'r') as file_object:
        logging.warning('opened file')
        text = file_object.read()
        soup = BeautifulSoup(text, "html.parser")
        return extract_forecasts(soup, 6)

def reload_cache_file(url):
    response = http.request('GET', url)
    with open(weather_cache_file, 'w') as file_object:
        soup = BeautifulSoup(response.data, "html.parser")
        text = extract_forecasts(soup, 6)            
        file_object.write(text)
        return text
    
def get_web_forecast_v2(url):
    if os.path.exists(weather_cache_file):
        fileCreation = os.path.getctime(weather_cache_file)
        now = time.time()
        fourhours_ago = now - 60*60*4
        if fileCreation > fourhours_ago:
            logging.warning('re using file cache')
            with open(weather_cache_file, 'r') as file_object:
                text = file_object.read()
                return Markup(text)
        else:
            logging.warning('refreshing file')
            os.remove(weather_cache_file)
            return reload_cache_file(url)        
    else:
        logging.warning('creating file for first time')
        return reload_cache_file(url)


