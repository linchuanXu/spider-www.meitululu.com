# -*- coding: utf-8 -*-

import url_manager
import html_downloader
import html_parser
import html_output
import urllib.request
import winsound

from setting import urls_person,urls_item

#https://www.meitulu.com/

class Spider(object):

    def __init__(self):#创建URL管理器+下载器+解析器+输出器
        self.url_mannager = url_manager.url_manager()
        self.html_downloader = html_downloader.html_downloader()
        self.html_parser = html_parser.html_parser()
        self.html_output = html_output.html_output()

# person
class Spider_person(Spider): # https://www.meitulu.com/t/wenxue-cher/
    def crew(self,url_person):
        html_cont = self.html_downloader.download(url_person)
        item_urls = self.html_parser.parser_item(html_cont)
        img_spider = Spider_root()
        for item_url in item_urls:
            img_spider.crew(item_url)






#item_root
class Spider_root(Spider):#首页面找到所有jpg地址 https://www.meitulu.com/item/7984.html
    def crew(self,url_root):
        self.url_mannager.add_url(url_root)#加入第一个网页
        count =0

        while self.url_mannager.is_not_empty():#循环管理器里面的所有网页
            url = self.url_mannager.get_url()            
            #下载数据
            html_cont = self.html_downloader.download(url)
            #获得主题 网址 图片
            if count == 0:
                file_name = self.html_parser.parser_title(html_cont)
                print('now: '+file_name)
            new_urls , new_img_urls = self.html_parser.parser_nexturl_imgs(html_cont)
            self.url_mannager.add_urls(new_urls)            
            for new_img_url in new_img_urls:
                img_name , img_data = self.html_downloader.download_img(url_root,new_img_url)
                if img_data != 0 and img_name!=0:
                    self.html_output.collect_img(file_name,img_name,img_data)

            count = count+1
        #self.html_output.output_imgurls()


if __name__ == "__main__":
    #测试下载器
    #dl = html_downloader.html_downloader()
    #print(dl.download('https://www.meitulu.com/item/7984.html'))


    winsound.Beep(600,500)

    img_s = Spider_root()
    person_spider = Spider_person()

    for i in urls_item:
        img_s.crew(i)
        winsound.Beep(600,500)

    for i in urls_person: 
        person_spider.crew(i)
        winsound.Beep(600,500)

