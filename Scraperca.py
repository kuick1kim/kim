import requests
import json

# 카톡 디벨로퍼스 가서 로그인하기 https://developers.kakao.com/
# https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends
# https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message
# 나의 rest api 저기다가 입력하기 = 9b7c298769083f3a2c6a50a63998bc78

# https://kauth.kakao.com/oauth/authorize?client_id=9b7c298769083f3a2c6a50a63998bc78&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message

# 저것을 복사해서 붙여넣기
# 그럼 순간적으로 키가 나온다


#2.
with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}
call0 = '깃허브에서 카톡을 자동으로 보내기 연습중'

data = {"template_object" : json.dumps({ "object_type" : "text",
                                        "text" : call0 ,
                                        "link" : {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
        })
    }

response = requests.post(url, headers=headers, data=data)
print(response.status_code)

if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
