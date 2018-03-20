# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import codecs


# def getHttp(url):
#     try:
#         req = requests.get(url,timeout=60)
#         # soup = BeautifulSoup(req.content.encode('iso-8859-1').decode('gbk'), "html.parser")
#         return req.text
#     except Exception as e:
#         print e
#         return None


jsonDatalist = []
if __name__ == '__main__':
    '''
    游戏5
最新3
网络红人6
热门影视7
动物9
风景10
明星11
舞蹈12
卡通4
免费21

 {data:[{Code:"Cartoon",Name:"卡通动漫"}, 4
    {Code:"Game",Name:"游戏专区"},  5
    {Code:"InternetStar",Name:"网络红人"},   6
    {Code:"Movies",Name:"热门影视"}  7
    ,{Code:"Pet",Name:"动物萌宠"},  9
    {Code:"Scenery",Name:"风景名胜"}   10
    ,{Code:"Star",Name:"明星系列"},   11
    {Code:"SongDance",Name:"歌曲舞蹈"}, 12
    {Code:"Others",Name:"其他资源"}]}  
    
    '''
    cate = {6:"InternetStar",4:"Cartoon",5:"Game",7:"Movies",9:"Pet",10:"Scenery",11:"Star",12:"SongDance"}
    chromedriver = u'/usr/local/Sunanang/phantomjs/bin/phantomjs'
    driver = webdriver.PhantomJS(chromedriver)
    for i in cate.keys():
        categ = cate.get(i)
        url = 'http://api.open.itobike.com/cgi/api.ashx/data/list.json?page=%d' % i
        # print url
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        jsonData =  soup.getText()
        data = json.loads(jsonData)
        datas =  data['data']
        for i in datas:
            # print i
            imgUrl = i['pp']
            name = i['name']
            video = i['link']
            size = i['size']
            data = {
                "videoUrl":"%s" % video,
                "videoPic":"%s" % imgUrl,
                "size":"%d" % size,
                "name":"%s" % name.encode('utf-8'),
                "category": "%s" % categ
            }
            # print data
            jsonDatalist.append(data)

    data = json.dumps(jsonDatalist, ensure_ascii=False, encoding='UTF-8')
    fs = codecs.open('/Users/apple/Desktop/videoXxJson.json', "w+", "UTF-8")

    fs.write(data)
    fs.flush()
    fs.close()
