# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import sys
import codecs

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")


    baseUrl = 'http://cdnwpuc.shoujiduoduo.com/wallpaper/'
    jsonData = []

    fo = open('/Users/apple/Desktop/videoPP.txt')
    soup = BeautifulSoup(fo.read(), "html.parser")
    datalist = soup.find_all('uservideo')
    for i in datalist:
        category = None
        cate = i.get('cate')
        if '29' in cate:
            category = 'Cartoon'
        elif '11' in cate or '20' in cate or '3' in cate:  #11    20  3
            category = 'InternetStar'
        elif '13' in cate:
            category = 'Game'
        elif '25' in cate:
            category = 'Movies'
        elif '14' in cate:
            category = 'Pet'
        elif '18' in cate or '22' in cate or '17' in cate:   # 18  22  17
            category = 'Scenery'
        elif '12' in cate:
            category = 'Star'
        elif '28' in cate:
            category = 'SongDance'
        elif '26' in cate or '27' in cate or '21' in cate or '42' in cate or '19' in cate or '23' in cate:
            category = 'Others'
        if category != None:
            videoUrl = i.get('preview_url')
            name = i.get('name')
            videoPic = i.get('thumb')
            sizes = i.get('size')
            videoUrl = '%s%s' % (baseUrl,videoUrl)
            videoPic = '%s%s' % (baseUrl,videoPic)
            sizes = int(sizes) / 1048576
            # print videoUrl
            # print name
            # print videoPic
            # print size
            data = {
                "videoUrl":"%s" % videoUrl,
                "videoPic":"%s" % videoPic,
                "size":"%d" % sizes,
                "name":"%s" % name.encode('utf-8'),
                "category": "%s" % category
            }

            jsonData.append(data)
        # else:
            # print "+++++++++"
        print "==============================="

    data = json.dumps(jsonData, ensure_ascii=False, encoding='UTF-8')
    # print data
    # s = '%s' % json.loads(data)
    # s = s.encode('utf-8')

    # print s
    fs = codecs.open('/Users/apple/Desktop/videoJson.json', "w+", "UTF-8")
    # fs = open('/Users/apple/Desktop/videoJson.json','w+')
    fs.write(data)
    fs.flush()
    fs.close()
    fo.close()


    '''
    http://cdnwpuc.shoujiduoduo.com/wallpaper/
    [
        {
        “videoUrl”:””,
        “videoPic”:””
        “size”:””
        “name”:””
        “category”:””
        }
    
    
    ]
    
    {data:[{Code:"Cartoon",Name:"卡通动漫"},  29
    {Code:"Game",Name:"游戏专区"},  13
    {Code:"InternetStar",Name:"网络红人"},      11    20  3
    {Code:"Movies",Name:"热门影视"}  25
    ,{Code:"Pet",Name:"动物萌宠"},  14
    {Code:"Scenery",Name:"风景名胜"}   18  22  17
    ,{Code:"Star",Name:"明星系列"},  12
    {Code:"SongDance",Name:"歌曲舞蹈"}, 28
    {Code:"Others",Name:"其他资源"}]}   26 27 21  42 19 23
    
    
    <category name="美女" id="11" update_num="26" /> 
    <category name="情感" id="26" update_num="26" /> 
    <category name="文字" id="27" update_num="27" /> 
    <category name="自然风光" id="18" update_num="43" /> 
    <category name="物语" id="22" update_num="18" /> 
    <category name="明星名人" id="12" update_num="39" /> 
    <category name="性感" id="28" update_num="17" /> 
    <category name="卡通插画" id="29" update_num="20" /> 
    <category name="设计创意" id="21" update_num="21" /> 
    <category name="动漫游戏" id="13" update_num="37" /> 
    <category name="动物宠物" id="14" update_num="10" /> 
    <category name="品牌Logo" id="16" update_num="44" /> 
    <category name="汽车机械" id="15" update_num="42" /> 
    <category name="影视娱乐" id="25" update_num="11" /> 
    <category name="城市风情" id="17" update_num="18" /> 
    <category name="运动" id="20" update_num="32" /> 
    <category name="科技" id="19" update_num="26" /> 
    <category name="其它" id="23" update_num="45" /> 
    
    '''
