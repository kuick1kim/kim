import requests
import json
def post_message(channel, text): 
    SLACK_BOT_TOKEN = "xoxb-2112022842768-2085165280581-o9qnWyaY4yBVKZSZr5BhiMeR"
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
    post_message("#stock", "깃허브에서 자동으로 슬랙으로 메세지를 보내고 있습니다")