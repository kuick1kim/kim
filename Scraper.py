import requests
from pandas import DataFrame
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
from selenium import webdriver
import openpyxl 
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

date = str(datetime.now())
date = date[:date.rfind(':')].replace(' ', '_')
date = date.replace(':','시') + '분'




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(os.path.getcwd(__file__))
# query = input('검색 키워드를 입력하세요 : ')

# news_num = int(input('총 필요한 뉴스기사 수를 입력해주세요(숫자만 입력) : '))
# query = query.replace(' ', '+')


news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=수지' #네이버뉴스


req = requests.get(news_url)
soup = BeautifulSoup(req.text, 'html.parser')


news_dict = {}
idx = 0
cur_page = 1

print()
print('네이버 크롤링 중... 주기도문을 외우세요')
# area_list = [li.find('div', {'class' : 'news_area'}) for li in li_list]a_list
while idx < 50:
### 네이버 뉴스 웹페이지 구성이 바뀌어 태그명, class 속성 값 등을 수정함(20210126) ###
    
    table = soup.find('ul',{'class' : 'list_news'})
    li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})
    area_list = [li.find('div', {'class' : 'news_area'}) for li in li_list]
    # kkk = soup.find('[li.find('a', {'class' : 'dsc_thumb'}.get('src' + '.jpg')) for li in li_list]
    a_list = [area.find('a', {'class' : 'news_tit'}) for area in area_list]
    
    for n in a_list[:min(len(a_list), 50-idx)]:
        news_dict[idx] = {'title' : n.get('title'),
                          'url' : n.get('href') , '신문사' : str() }

                          
        idx += 1

    cur_page += 1

    pages = soup.find('div', {'class' : 'sc_page_inner'})
    next_page_url = [p for p in pages.find_all('a') if p.text == str(cur_page)][0].get('href')
    
    req = requests.get('https://search.naver.com/search.naver' + next_page_url)
    soup = BeautifulSoup(req.text, 'html.parser')

print('네이버 크롤링 완료')

print('데이터프레임 변환')




# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.getcwd()


with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(news_dict, json_file, ensure_ascii = False, indent='\t')
    


news_df = DataFrame(news_dict).T

folder_path = os.getcwd()
xlsx_file_name = 'NAVER_{}.xlsx'.format(date)

news_df.to_excel(xlsx_file_name)



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
content = "내용 없음"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

part = MIMEBase('application', "octet-stream")
with open('NAVER_{}.xlsx'.format(date), 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename='NAVER_{}.xlsx'.format(date)) # 첨부파일 이름
msg.attach(part)

# part = MIMEBase('application', "octet-stream")
# with open('news.json', 'rb') as file:
#     part.set_payload(file.read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment", filename='news.json') # 첨부파일 이름
# msg.attach(part)


# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()
print()
print('메일까지 잘......보냈습니다.')
