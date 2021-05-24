from bs4 import BeautifulSoup

import json

import requests
import re
import time, os
from datetime import datetime



date = str(datetime.now())
date = date[:date.rfind(':')].replace(' ', '_')
date = date.replace(':','시') + '분'






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

req = requests.get('https://www.yna.co.kr/safe/news')
time.sleep(3)
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')




# req = requests.get('https://www.yna.co.kr/safe/news')
# time.sleep(3)
# req.encoding= None
# html = req.content
# soup = BeautifulSoup(driver.page_source, 'html.parser')
datas = soup.select('#container > div > div.content01 > div > ul > li')
# print('There are %d reviews avaliable!' % len(datas))


data = {}


for title in datas:   
    bbb = title.find('h3')
    name = bbb.find_all('a')[0].text
    url = 'http:'+title.find('a')['href']
    name2 = title.find_all('p', class_='lead')[0].text
    name3 = name2.replace("\n","  ")
    data[name] = '기사요약-> ' + name3 + '   URL 주소는 여기---> ' + url
    # print(name)
    # print(url)
    # print(name2)


with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('뉴스기사 스크래핑 끝')




if __name__ == '__main__':
    post_message("#stock", "메세지가 도착하였습니다.")




# folder_path = os.getcwd()
# driver.get_screenshot_as_file('사람인1.png')
# driver.quit()
# os.startfile(folder_path)


# driver.quit()
