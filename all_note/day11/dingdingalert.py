#!/usr/bin/env python
# 这只是一个报警脚本， 还需要有报警动作来执行 这个 脚本
# 参考
import json
import requests
import sys

def send_msg(url, remiders, msg):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "msgtype": "text",
        "at": {
            "atMobiles": remiders,
            "isAtAll": False,
        },
        "text": {
            "content": msg,
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    msg = sys.argv[1]
    remiders = []
    url = '钉钉机器人的URL'
    print(send_msg(url, remiders, msg))
# 别忘了
# [root@node2 ~]# chmod +x /usr/local/share/zabbix/alertscripts/dingalert.py