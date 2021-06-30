import requests 
from bs4 import BeautifulSoup 
import re
from datetime import datetime
import pandas as pd
from pandas import DataFrame
import os
from datetime import datetime
import time
import csv

import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)

date = str(datetime.now())
date = date[:date.rfind(':')].replace(' ', '_')
date = date.replace(':','시') + '분'



url0 = 'http://www.stocksignals.co.kr:8080/stockguest/0102.php'
url = url0

raw = requests.get(url)
html = BeautifulSoup(raw.text, 'html.parser' )
table = html.select(".boxstyle")[2]
row = table.select("tr" )[2] #10번째 줄을 의미함 자본이 늘어나는지
table2 = row.select(".boxstyle") #1번째 칸 추출을 의미함 자본이 늘어나는지
# rowrow = table2.select("td")

infoTable = row.find("table",{"class":"boxstyle"})


df = pd.DataFrame()
infoPrint =[]
for a in infoTable.find_all("tr"):
    infolist = []
    for b in a.find_all("td"):
        info = b.get_text()
        infolist.append(info)
    # print(infolist)
    infoPrint.append(infolist)
    # df = df.append(infolist)
# print(infoPrint)
df2 = df.append(infoPrint)

save_df = pd.DataFrame(df2)
print(df2)
df2 = df2.replace('°³ÀÎ','개인').replace('Åõ½Å','투신').replace('Áõ±Ç','기관').replace('¿Ü±¹ÀÎ','외국인').replace('ÄÝ¿É¼Ç (´ÜÀ§:°è¾à¼ö)','콜옵션').replace('Ç²¿É¼Ç (´ÜÀ§:°è¾à¼ö)','풋옵션').replace('Çà»ç°¡','행사가').replace('Á¾°¡','현재가격')

# /////////////////////////////////////////////////
# /////////////////////////////////////////////////
# /////////////////////////////////////////////////

# /////////////////////////////////////////////////
url = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=1'

raw = requests.get(url)
html = BeautifulSoup(raw.text, 'html.parser' )

infolist2 = []
table = html.select(".table-col.case02")

df = pd.DataFrame()
infoPrint =[]
for a in html.find_all("tr"):
    infolist = []
    for b in a.find_all("td"):
        info = b.get_text()
        infolist.append(info)
    # print(infolist)
    infoPrint.append(infolist)
df = df.append(infoPrint, ignore_index=True)
# print(infoPrint)
# print(df)




url3 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=3'

raw = requests.get(url3)
html = BeautifulSoup(raw.text, 'html.parser' )

infolist2 = []
table = html.select(".table-col.case02")

df3 = pd.DataFrame()
infoPrint =[]
for a in html.find_all("tr"):
    infolist = []
    for b in a.find_all("td"):
        info = b.get_text()
        infolist.append(info)
    # print(infolist)
    infoPrint.append(infolist)
df3 = df3.append(infoPrint, ignore_index=True)
# print(infoPrint)
# print(df3)


url5 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=5'

raw = requests.get(url5)
html = BeautifulSoup(raw.text, 'html.parser' )

infolist2 = []
table = html.select(".table-col.case02")

df5 = pd.DataFrame()
infoPrint =[]
for a in html.find_all("tr"):
    infolist = []
    for b in a.find_all("td"):
        info = b.get_text()
        infolist.append(info)
    # print(infolist)
    infoPrint.append(infolist)
df5 = df5.append(infoPrint, ignore_index=True)
# print(infoPrint)
# print(df5)



url10 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=10'

raw = requests.get(url10)
html = BeautifulSoup(raw.text, 'html.parser' )

infolist2 = []
table = html.select(".table-col.case02")

df10 = pd.DataFrame()
infoPrint =[]
for a in html.find_all("tr"):
    infolist = []
    for b in a.find_all("td"):
        info = b.get_text()
        infolist.append(info)
    # print(infolist)
    infoPrint.append(infolist)
df10 = df10.append(infoPrint, ignore_index=True)
# print(infoPrint)
# print(df10)


url20 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=20'

raw = requests.get(url20)
html = BeautifulSoup(raw.text, 'html.parser' )

infolist2 = []
table = html.select(".table-col.case02")

df20 = pd.DataFrame()
infoPrint =[]
for a in html.find_all("tr"):
    infolist = []
    for b in a.find_all("td"):
        info = b.get_text()
        infolist.append(info)
    # print(infolist)
    infoPrint.append(infolist)
df20 = df20.append(infoPrint, ignore_index=True)
# print(infoPrint)
# print(df20), print(df)


frames = [df, df3, df5, df10, df20]
result = pd.concat(frames)
# result = pd.set_option('display.max_columns', None)

print(result)

save_df = pd.concat([df,df3,df5,df10,df20], axis=1)








# folder_path = os.getcwd()
df2.to_csv('오늘의옵션가격{d}.csv'.format(d = date), index=False, encoding='utf-8-sig')
# os.startfile(folder_path)
save_df.to_csv('오늘의옵션매매동향{d}.csv'.format(d = date), index=False, encoding='utf-8-sig')





# 보내는 사람 정보
me = "kuick1@hanmail.net"
my_password = "kmskms4869@"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.daum.net')
s.login(me, my_password)

# 받는 사람 정보
you = "kuick1@hanmail.net"

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "김민상이 오늘의 옵션가격 보냈습니다"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
link1 = "http://www.stocksignals.co.kr:8080/stockguest/0102.php"

link2 = "https://finance.daum.net/domestic/investors/DERIVATIVES"
content1 = str(link2) + "         " +str(link1) + "         " + str(df2) +"                                                                " + str(result)
part2 = MIMEText(content1, 'plain')
msg.attach(part2)





part = MIMEBase('application', "octet-stream")
with open('오늘의옵션가격{d}.csv'.format(d = date), 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename='오늘의옵션가격{d}.csv'.format(d = date)) # 첨부파일 이름
msg.attach(part)

part = MIMEBase('application', "octet-stream")
with open('오늘의옵션매매동향{d}.csv'.format(d = date), 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename='오늘의옵션매매동향{d}.csv'.format(d = date)) # 첨부파일 이름
msg.attach(part)





# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()
print()
print('이메일까지 잘......보냈습니다.')
