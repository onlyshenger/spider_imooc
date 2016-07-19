#!D:\Python27\python
# -*- coding: utf-8 -*-

from spider.spiderman import SpiderMan
from time import sleep


if __name__=="__main__":
    print u'#####################################################################'
    print u"#慕课网视频抓取器"
    print u"author:七夜"
    print u"博客：http://blog.csdn.net/qiye_/和http://www.cnblogs.com/qiyeboy/ 同步更新 "
    print u"微信公众号:qiye_python"
    print u"github:https://github.com/qiyeboy/"
    print u"#到慕课网官网打开想要下载的课程的章节列表页面，查看当前url链接"
    print u"#例如http://www.imooc.com/learn/615，则课程编号为615"
    print u"#####################################################################"


    # IDs = [317,475,550,458,581,457,532,563,416,317,456]
    # IDs = [475,550,458,581,457,532,563,416,317,456,622,497,526,296,292,293,272,228,415,
    #        391,356,456,478,257,202,261,214,165,199,146,145,112,]
    # IDs = [272,228,415,391,356,456,478,257]
    IDs = [208,390]
    COURSEURL = "http://www.imooc.com/learn/"
    for ID in IDs:
        spider = SpiderMan()
        url = COURSEURL+str(ID)
        spider.cmdshow_gbk(url)
        sleep(600)
    # spider.crawl("http://www.imooc.com/learn/317")
