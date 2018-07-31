# -*- coding: utf-8 -*-
import os
import requests
import sys
import io

class html_output(object):

    def collect_imgurls(self,urls):
        for i in urls:
            if i[-6:] != '/0.jpg':
                self.img_urls.append(i)


    def collect_img(self,file_name,name,data):#输入文件数据，下载到文件
        file_name = file_name.replace('\\','-')
        file_name = file_name.replace('/','-')
        path = 'image\\'+ file_name+'\\'
        if not os.path.exists(path):
            os.makedirs(path)
        f = open( path + name , 'wb')
        f.write(data)
        #print(name+':'+ str(round(len(data)/1000))+'kb',end=' ')
            

