import requests
from pandas import DataFrame
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
from selenium import webdriver
import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders

date = str(datetime.now())
date = date[:date.rfind(':')].replace(' ', '_')
date = date.replace(':','시') + '분'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("window-size=1100,2800")
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)




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

try :
    url20 = 'http://www.stocksignals.co.kr:8080/stockguest/0102.php'
    driver.get(url20)
    time.sleep(3)
    driver.get_screenshot_as_file('option.jpg')
except: 
    pass

try :
    url20 = 'https://finance.daum.net/domestic/kospi'
    driver.get(url20)
    time.sleep(3)
    driver.get_screenshot_as_file('option1.jpg')
except: 
    pass


chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1100,2800")
action = ActionChains(driver)

try :
    url20 = 'https://finance.daum.net/domestic/investors/DERIVATIVES'
    driver.get(url20)
    time.sleep(3)
    send_butten = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/div[2]/div/a[2]')
    
    action.move_to_element(send_butten).click().perform()
    time.sleep(3)
    driver.get_screenshot_as_file('opt_daum1.jpg')


    action = ActionChains(driver)
    send_butten2 = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/div[3]/div[2]/div/div/a[1]')
    action.move_to_element(send_butten2).click().perform()
    time.sleep(1)
    action = ActionChains(driver)
    send_butten22 = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/a[1]')
    action.move_to_element(send_butten22).click().perform()
    time.sleep(0.5)
    action = ActionChains(driver)
    send_butten23 = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/div[5]/div[2]/div/div/a[1]')
    action.move_to_element(send_butten23).click().perform()
    time.sleep(2)
    driver.get_screenshot_as_file('opt_daum2.jpg')    
except: 
    pass
driver.quit()



# ///////////////////////////////////////////////////
# /////////////////////////////////////////////////
# /////////////////////////////////////////////////
# /////////////////////////////////////////////////


# 보내는 사람 정보
# me = "kuick1@naver.com"
my_password = "kmskms4869@"
me = "kuick1@hanmail.net"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.daum.net')
s.login(me, my_password)

# 받는 사람 정보
you = "kuick1@naver.com"

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "{d} 오늘의 옵션가격".format(d=date)
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "           "
part2 = MIMEText(content, 'plain')
msg.attach(part2)




WHOLE_URL=['option1.jpg','opt01.jpg','opt03.jpg','opt05.jpg','opt10.jpg','opt20.jpg','option.jpg','opt_daum1.jpg','opt_daum2.jpg']

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







