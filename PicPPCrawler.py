# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import codecs

jsonList = []

def getHttp(url):
    try:
        req = requests.get(url,timeout=60)
        # soup = BeautifulSoup(req.content.encode('iso-8859-1').decode('gbk'), "html.parser")
        return req.text
    except Exception as e:
        print e
        return None

if __name__ == '__main__':
    menuUrl = 'http://service.aibizhi.adesk.com/v1/vertical/category?adult=false&first=1'
    jsonDatas = getHttp(menuUrl)
    data = json.loads(jsonDatas)
    dataLists = data["res"]
    category = dataLists["category"]
    for i in category:
        ename = i["ename"]
        id = i["id"]
        codeUrl = "http://service.aibizhi.adesk.com/v1/vertical/category/" \
              "%s/vertical?limit=30&adult=false&first=1&order=new" % id;
        jsons = getHttp(codeUrl)
        datas = json.loads(jsons)
        jsonDataList = datas["res"]["vertical"]
        for i in jsonDataList:
            thumb = i["thumb"]
            img = i["img"]
            wp = i["wp"]
            # print thumb
            # print img
            # print wp
            # print ename
            data = {
                "thumb": "%s" % thumb,
                "ImgUrl": "%s" % img,
                "basePicUrl": "%s" % wp,
                "category": "%s" % ename
            }
            jsonList.append(data)

    data = json.dumps(jsonList, ensure_ascii=False, encoding='UTF-8')
    fs = codecs.open('/Users/apple/Desktop/PicJson.json', "w+", "UTF-8")

    fs.write(data)
    jsonList[:] = []
    fs.flush()
    fs.close()

