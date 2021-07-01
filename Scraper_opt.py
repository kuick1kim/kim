import requests
from pandas import DataFrame
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
from selenium import webdriver
import time
import codecs

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders

date = str(datetime.now())
date = date[:date.rfind(':')].replace(' ', '_')
date = date.replace(':','시') + '분'
options = webdriver.ChromeOptions()


options.add_argument("--headless")
options.add_argument("window-size=1000,2500")

driver = webdriver.Chrome('c:\kim\selenium\chromedriver.exe', chrome_options=options)

url1 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=1'
driver.get(url1)
time.sleep(3)
driver.get_screenshot_as_file('opt01.jpg'.format(date))

url3 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=3'
driver.get(url3)
time.sleep(3)
driver.get_screenshot_as_file('opt03.jpg'.format(date))

url5 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=5'
driver.get(url5)
time.sleep(3)
driver.get_screenshot_as_file('opt05.jpg'.format(date))

url10 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=10'
driver.get(url10)
time.sleep(3)
driver.get_screenshot_as_file('opt10.jpg'.format(date))

url20 = 'http://www.paxnet.co.kr/stock/sise/trend/subject?searchTerm=20'
driver.get(url20)
time.sleep(3)
driver.get_screenshot_as_file('opt20.jpg'.format(date))

driver.quit()




# ///////////////////////////////////////////////////
# /////////////////////////////////////////////////
# /////////////////////////////////////////////////
# /////////////////////////////////////////////////


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
msg['Subject'] = "김민상이 오늘의 옵션가격 사진으로 보냄"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "           "
part2 = MIMEText(content, 'plain')
msg.attach(part2)




WHOLE_URL=['opt01.jpg','opt03.jpg','opt05.jpg','opt10.jpg','opt20.jpg']

for i in range(len(WHOLE_URL)):
    part = MIMEBase('application', "octet-stream")
    with open(WHOLE_URL[i], 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename=WHOLE_URL[i]) # 첨부파일 이름
    msg.attach(part)






# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()
print()
print('이메일까지 잘......보냈습니다.')















