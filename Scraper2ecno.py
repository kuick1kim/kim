from bs4 import BeautifulSoup
import json
import requests
import re
import time, os
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from pandas import DataFrame


pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# pd.set_option('display.max_rows')
print('뉴스기사 스크래핑 시작')

df = pd.DataFrame(columns=['일반기사제목', '기사내용', '기사링크'])
data = {}

for p in range(1, 2+1, 1): #2개임 현재
    req = requests.get("https://www.yna.co.kr/news/{p}".format(p = p))
    req.encoding= None
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select('#container > div > div > div.section01 > section > div.list-type038 > ul > li')
    print('There are %d reviews avaliable!' % len(datas))
    for title in datas:   
        bbb2 = title.find("div" , class_='item-box01')
        bbb1 = title.find("div" , class_='news-con')
        try :
            name99 = bbb1.find_all('a')[0].text.replace('\n', '')
            name = name99.replace('\"', '>" ')
            url = 'http:'+title.find('a')['href']
            name2 = title.find_all('p', class_='lead')[0].text
            name3 = name2.replace('\n', '')
        except :
            pass
        data[name] = '기사요약-> ' + name3 + '            URL 주소는 여기---> ' + url
        df = df.append({
        '일반기사제목': name,
        '기사내용': name3,
        '기사링크': url
    }, ignore_index=True)
    print()   
    print()
    print()
        
print('일반기사 스크랩 완료')


# 경제뉴스 모으기
df2 = pd.DataFrame(columns=['경제기사제목', '기사내용', '기사링크'])
data2 = {}
for p in range(1, 2+1, 1): #2개임 현재
    reqe = requests.get("https://www.yna.co.kr/economy/all/{p}".format(p = p))
    reqe.encoding= None
    html = reqe.content
    soup = BeautifulSoup(html, 'html.parser')
    datas2 = soup.select('#container > div > div > div.section01 > section > div.list-type038 > ul > li')
    print('There are %d reviews avaliable!' % len(datas2))
    for title in datas2:   
        bbb2 = title.find("div" , class_='item-box01')
        bbb1 = title.find("div" , class_='news-con')
        try :
            name99 = bbb1.find_all('a')[0].text.replace('\n', '')
            namee = name99.replace('\"', '>" ')
            urle = 'http:'+title.find('a')['href']
            name2 = title.find_all('p', class_='lead')[0].text
            namee3 = name2.replace('\n', '')
        except :
            pass
        data2[namee] = '기사요약-> ' + namee3 + '            URL 주소는 여기---> ' + urle
        df2 = df2.append({
        '경제기사제목': namee,
        '기사내용': namee3,
        '기사링크': urle
    }, ignore_index=True)
        
        


print('경제기사 스크랩 완료')




with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')
with open(os.path.join(BASE_DIR, 'news2e.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data2, json_file, ensure_ascii = False, indent='\t')
    # print('저장됨')

print('뉴스기사 스크래핑 끝')

news_df = DataFrame(df).T
news_df = DataFrame(df2).T
# df = pd.set_option('display.max_rows')
# news_df = df.loc[:,['A','B','c']]
# folder_path = os.getcwd()
# print(df)
# print(df2)
# xlsx_file_name = 'NAVER_{}.xlsx'.format(date)
# news_df.to_excel(xlsx_file_name)









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
msg['Subject'] = "김민상이 보냈습니다"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = str(df) + str(df2)
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# content2 = str(df2)
# part22 = MIMEText(content2, 'plain')
# msg.attach(part22)
# print(df2)



part = MIMEBase('application', "octet-stream")
with open('news.json', 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename='news.json') # 첨부파일 이름
msg.attach(part)
# with open('news2e.json', 'rb') as file:
#     part22.set_payload(file.read())
# encoders.encode_base64(part22)
# part.add_header('Content-Disposition', "attachment", filename='news2e.json') # 첨부파일 이름
# msg.attach(part22)


# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()
print()
print('이메일까지 잘......보냈습니다.')


