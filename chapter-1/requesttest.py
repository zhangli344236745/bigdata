# -*- coding:utf-8 -*-'
import requests
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
respone = requests.get(url)
#print respone.content
print respone.status_code
print respone.headers['content-type']
print respone.encoding

soup = BeautifulSoup(respone.content,'html.parser')
print soup.prettify()
print soup.body['link']
print soup.find_all(id="kw")[0]['class']
print soup.select('input#kw')[0]
