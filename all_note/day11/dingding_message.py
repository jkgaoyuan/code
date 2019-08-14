###钉钉机器人推送消息
####核心就是 request.post + json ,,,,通过post 将要发送的内容推送到 url对应的服务上
###不管 钉钉机器人. 图灵机器人  天气查询
import requests
import json
url = 'https://oapi.dingtalk.com/robot/send?access_token=06ccf89ab7a8a4e4ac340a3e1eb376a83b5b73dcaa03b5f7c7b06006c81a0b62'
headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "text",   # 文本消息
#     "text": {
#         "content": "@底下哥牛逼 @王凯... nsd1903///底下哥牛逼"
#     },
#     "at": {
#         "atMobiles": [
#             # "王凯",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }
##dunp上传 load 加载

data = {
    "msgtype": "link",
    "link": {
        "text": """？""",
        "title": "时代的火车向前开",
        "picUrl": "http://img03.sogoucdn.com/v2/thumb/resize/w/640/t/2/retype/ext/jpg/q/75?appid=200556&url=http%3A%2F%2Fimg03.sogoucdn.com%2Fapp%2Fa%2F200841%2F38fba83050849149921702a35451022c",
        "messageUrl": "http://pic.sogou.com"
    }
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())