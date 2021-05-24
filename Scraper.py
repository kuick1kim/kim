from bs4 import BeautifulSoup
import json
import requests
import re
import time, os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('뉴스기사 스크래핑 시작')

def post_message(channel, text): 
    SLACK_BOT_TOKEN = "xoxb-2112022842768-2085165280581-QPcIPXDvyRNajovLGETxPjSw"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
        }
    payload = {'channel': channel,'text': text}
    r = requests.post('https://slack.com/api/chat.postMessage', 
        headers=headers, 
        data=json.dumps(payload)
        )


if __name__ == '__main__':
    post_message("#stock", "새로운 뉴스 스크랩 끝.")

req = requests.get('https://www.yna.co.kr/news?site=navi_latest_depth01')
time.sleep(3)
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')



datas = soup.select('#container > div > div > div.section01 > section > div.list-type038 > ul > li')

data = {}

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


with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')


print('뉴스기사 스크래핑 끝')
print('뉴스기사 스크래핑 끝')
print('뉴스기사 스크래핑 끝')

