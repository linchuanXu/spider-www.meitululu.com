# -*- coding: utf-8 -*-
import requests

class html_downloader(object):
    def download(self,url):##############解决Requests中文乱码
        req = requests.get(url)
        req.encoding='utf-8'
        data = req.text
        
        return data

    def download_img(self,Refer,url_image):
        #防盗链header！！！
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        headers['Referer'] = Refer
        

        img_r = requests.get(url_image , headers=headers )
        if img_r.status_code == 200:
            name = url_image.split('/')[-1]
            return name,img_r.content
        else:
            return 0,0


