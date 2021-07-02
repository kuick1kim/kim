from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import smtplib
from email.mime.text import MIMEText
import os

from os.path import join, dirname
from dotenv import load_dotenv


# 고정 변수
dirver_loc = os.path.realpath(__file__)[:-10]+'/chromedriver'

joonggonara_url = 'https://cafe.naver.com/joonggonara.cafe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L%26viewType=pc'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(dirver_loc, options=options)

driver.get(joonggonara_url)
driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main_headless.png')

print(joonggonara_url)

driver.quit()
