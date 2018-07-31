# -*- coding: utf-8 -*-
import re

class html_parser(object):
    def parser_nexturl_imgs(self,cont):#找到下一页的网址 和 本页图片地址
        datas = []
        urls = []
        if cont is None:
            return None

        #找下一页地址
        rule_url = 'item/\d+_\d+\.html'#结果是item的
        result_url = re.findall(rule_url,cont)
        for url in result_url:
            urls.append('https://www.meitulu.com/' + url)

        #找图片下载地址
        rule_image = 'https://mtl.ttsqgs.com/images/img/.*?jpg'
        result_img = re.findall(rule_image,cont)       
        for img_url in result_img:            
            if img_url.split('/')[-1] != '0.jpg':
                datas.append(img_url)
        
        

        return urls,datas
    def parser_title(self,cont):
        rule_title = '<h1>(.*?)</h1></div>'
        title = re.findall(rule_title,cont)  
        return title[0]
    def parser_item(self,cont):#从个人首页找到item_urls
        rule_item = 'https://www.meitulu.com/item/\d+.html'
        items = re.findall(rule_item,cont)  
        items = list(set(items))
        return items
