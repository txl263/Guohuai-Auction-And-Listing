# coding: utf-8
from __future__ import unicode_literals
# author: Eric
#
# fun: 从百度地图webAPI获取随机地址
import json
import urllib2
import httplib
import random
import password
x = random.uniform(30, 40)
y = random.uniform(80, 115)
#print str(x)

def getAddress1():
    pass
    #url = 'http://api.map.baidu.com/geocoder/v2/?callback=renderReverse'
    url = 'http://api.map.baidu.com/geocoder/v2/?'
    #back='&callback=renderReverse&location='  
    back='&location='  
    #location='34.992654,108.589507'
    location = str(x) + ',' + str(y)
    output = '&output=json&pois=0'  

    #http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=39.983424,116.322987&output=json&pois=1&ak=

    url = url +back + location + output + '&ak=' + password.ak
    print url
    temp = urllib2.urlopen(url)
    #console.log(data)  
    hjson = json.loads(temp.read())  
    location = hjson["result"]["formatted_address"] #省，市，县  
    print location
    info = hjson["result"]["sematic_description"]  #详细描述  
    print info

def getAddress():
    companyName = ''
    try:
        url = 'http://api.map.baidu.com/place/v2/search?query=公司,企业&region=北京&page_size=1&scope=1'
        #back='&callback=renderReverse&location='  
        back='&location='  
        #location='34.992654,108.589507'
        location = str(x) + ',' + str(y)
        pagenum = '&page_num=' + str(random.randint(1, 300))
        output = '&output=json'  

        #http://api.map.baidu.com/place/v2/search?公司,企业&region=北京&page_size=1&page_num=343%20&output=json&ak=F8mG47SpoaGNdswXhByZHLs9YRQiwnLT

        url = url + pagenum + output + '&ak=' + password.ak
        print url
        temp = urllib2.urlopen(url)
        #console.log(data)  
        hjson = json.loads(temp.read())
        companyName = hjson["results"]["name"] #省，市，县  
        print location
        address = hjson["results"]["address"]  #详细描述  
        print info
    except:
        pass
    return companyName

if __name__ == '__main__':
    name = getAddress()
    print name