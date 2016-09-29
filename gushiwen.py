# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:19:36 2016

@author: ustc
"""

import urllib.request
from bs4 import BeautifulSoup
import re
import os


list1 = [x for x in range(80000,90000)]

for index_number in list1:

    try:
    
        url = 'http://so.gushiwen.org/view_'
        url = url+str(index_number)+'.aspx'
            
            
            
        data = urllib.request.urlopen(url).read()
        data = data.decode('UTF-8')
        
        soup = BeautifulSoup(data,"lxml")
        
        try:
            main3 = soup.find("div",class_='main3')
            
            timu = main3.find("div",class_='son1')     #题目
            yuanwen = main3.find("div",class_='son2')  #原文
            yuanwen_text = yuanwen.prettify()
            yuanween_text = re.sub(r'<br />','\n',yuanwen_text)
            yuanwen = BeautifulSoup(yuanwen_text,"lxml")
            
            
            qita = main3.find_all("div",class_='son5')
            
            try:
                address = str(index_number)+'.txt'
                f = open(address, 'w')
                f.write(timu.get_text())
                f.write(yuanwen.get_text())
                
                #print(timu.get_text())
                #print(yuanwen.get_text())
            
            
                for i in qita:
                    pattern1 = re.compile(r'javascript:showSon5FY\(\d+\)')
                    #print(i.prettify())    
                    id_string1 = pattern1.findall(i.prettify())
                    #print(id_string)
                    pattern2 = re.compile(r'javascript:showSon5SX\(\d+\)')    
                    id_string2 = pattern2.findall(i.prettify())
                    
                    
                    if id_string1:
                        id_number = re.findall('\d+',id_string1[0])
                        #print('id_number:'+id_number[1])
                        url_new = 'http://so.gushiwen.org/shiwen/ajaxfanyi.aspx?id=' + id_number[1]
                        fanyi = urllib.request.urlopen(url_new).read()
                        fanyi = fanyi.decode('UTF-8')
                        fanyi_text = BeautifulSoup(fanyi,"lxml")
                        
                        
                        fanyi_text = fanyi_text.prettify()
                        fanyi_text = re.sub(r'<br />','\n',fanyi_text)
                        fanyi_text = BeautifulSoup(fanyi_text,"lxml")
                        #print(fanyi_text.get_text())
                        f.write(fanyi_text.get_text())
                    elif id_string2 :
                        id_number = re.findall('\d+',id_string2[0])
                        #print('id_number:'+id_number[1])
                        url_new = 'http://so.gushiwen.org/shiwen/ajaxshangxi.aspx?id=' + id_number[1]
                        shangxi = urllib.request.urlopen(url_new).read()
                        shangxi = shangxi.decode('UTF-8')
                        shangxi_text = BeautifulSoup(shangxi,"lxml")
                        
                        
                        shangxi_text = shangxi_text.prettify()
                        shangxi_text = re.sub(r'<br />','\n',shangxi_text)
                        shangxi_text = BeautifulSoup(shangxi_text,"lxml")
                        #print(shangxi_text.get_text())
                        f.write(shangxi_text.get_text())
                    else:
                        zuozhe = i.get_text()
                        f.write(zuozhe)
                        
                        
                    
                    
                    
                    
                f.close()
                print(index_number)
            except Exception as e:
                print(e)            
                f.close()
                os.remove(address)
        
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)




'''
address = str(index_number)+'.txt'
        f = open(address, 'w')
        f.write(str1)
        f.write('\n')
        f.write(str2)
        f.write('\n')
        
        for x in str3.split():
            f.write(x)
            f.write('\n')
        
        f.close()
str3 =  re.sub(r'[0-9a-z<>/\s]+',"",pattern3.findall(data)[0])
for i in qita:
    
    pattern1 = re.compile(r'javascriptshowson5sx(\d+)')
    shangxi = pattern1.findall(i.contents)
    
    if  shangxi:   
        id_number = re.findall('\d+',shangxi[0])
        url_new = 'http://so.gushiwen.org/shiwen/ajaxfanyi.aspx?id=' + id_number
        shangxi_text = urllib.request.urlopen(url_new).read()
        shangxi_text = shangxi_text.decode('UTF-8')
        print(shangxi_text.get_text())
       
    else:
        print(i.get_text())

'''