# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:30:01 2018

@author: asus
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:28:06 2018

@author: asus
"""

import os
import re

import requests
from bs4 import BeautifulSoup

#from selenium import webdriver
import pandas as pd
import time

str1="http://search.51job.com/list/"
str2=",000000,0000,"
workyear_str=",%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear="
degreefrom_str="&cotype=99&degreefrom="
jobterm_str="&jobterm=01"
last_str="&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

city_code=['010000',
'020000',
'030000',
'040000',
'050000',
'060000',
'070000',
'080000',
'090000',
'100000',
'110000',
'120000',
'130000',
'140000',
'150000',
'160000',
'170000',
'180000',
'190000',
'200000',
'210000',
'220000',
'230000',
'240000',
'250000',
'260000',
'270000',
'280000',
'290000',
'300000',
'310000',
'320000',
'330000',
'340000',
'350000',
]
salary_range=['01','02','03','04','05','06','07','08','09','10','11','12']
workyear=['01','02','03','04','05']
degreefrom=['01','02','03','04','05','06']
industry=['01',
'02',
'03',
'04',
'05',
'06',
'07',
'08',
'09',
'10',
'11',
'12',
'13',
'14',
'15',
'16',
'17',
'18',
'19',
'20',
'21',
'22',
'23',
'24',
'25',
'26',
'27',
'28',
'29',
'30',
'31',
'32',
'33',
'34',
'35',
'36',
'37',
'38',
'39',
'40',
'41',
'42',
'43',
'44',
'45',
'46',
'47',
'48',
'49',
'50',
'51',
'52',
'53',
'54',
'55',
'56',
'57',
'58']


output1 = pd.DataFrame(columns=['city', 'industry', 'income','workyear','degreefrom','quantity','url_link'])
#str1="http://search.51job.com/list/"
#str2="000000,0000,"
#workyear=",%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear="
#degreefrom="&cotype=99&degreefrom="
#jobterm="&jobterm=01"
#last_str="&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

for i in range(len(city_code)):
    for j in range(len(industry)):
        for k in range(len(salary_range)):
            for l in range(len(workyear)):
                for m in range(len(degreefrom)):
                    url_link = str1+city_code[i]+str2+industry[j]+",9,"+salary_range[k]+workyear_str+workyear[l]+degreefrom_str+degreefrom[m]+jobterm_str+last_str
                    time.sleep(1)
                    print(url_link)
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
                    req = requests.get(url=url_link, headers=headers)
                    req.encoding = 'gbk'
                    html = req.text
                   
                    bf = BeautifulSoup(html, 'lxml')
                    
                    pattern=re.compile(r"共\d*页")
                    result=re.findall(pattern,bf.get_text())
                    print(result)
                    
                    data = {
                    'city':city_code[i],
                    'industry':industry[i],
                    'income':salary_range[i],
                    'workyear':workyear[i],
                    'degreefrom':degreefrom[i],
                    'quantity':result,
                    'url_link':url_link
                    }
                    output1 = output1.append(pd.Series(data), ignore_index=True)
  
output1.to_csv("51job_result.csv", encoding="gbk", index=False) 




