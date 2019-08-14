import requests
import json
url = 'http://192.168.1.23/api_jsonrpc.php'  ###写api 文件的 url
headers = {'Content-Type': 'application/json-rpc'}  ####这是个字典 key:values


#### 下面的zabbix 参数写法 可以在这个网站上面查到模板
#https://www.zabbix.com/documentation/3.4/zh/manual -> 19. API
###################################
# 有些数据不需权限，可以直接获取，如版本号
# 查看结果，主要看result的值
# data = {
#     "jsonrpc": "2.0",      # 固定值
#     "method": "apiinfo.version",
#     "params":[],       #参数
#     "id": 1011        # 随便填一个数字，表示任务ID
# }

#########获取主机令牌 信息 信息在result中返回
###每获取一次令牌返回的令牌信息是会变化的 并且令牌信息的有效期是有时间限制的,具体需要查询
####zabbix 网页端
#### 配置方法：
#### "Administration" (Top Menu) -> "Users" (Sub Menu) -> "Username" -> "Auto-logout"
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 'result': '3a82ae7bbdaf007210ff8d6c6673b218'

#############
#####通过zabbix 查询主机信息
###通过下面的hosts[] 部分来配置
####范例 https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/host/get /// 第一个request

####主要查看 result , 结果是一个列表包含字典, 每个字典是一台主机 返回信息包括 hostid  host群组  等
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [                 #####限制条件
#                 "Zabbix server",
#                 "Linux server"
#             ]
#         }
#     },
#     "auth": "3a82ae7bbdaf007210ff8d6c6673b218",  ###这里写获取到的令牌
#     "id": 1
# }
####################################
###### 删除id为10257的主机
# data = data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10257",
#         # "32"
#     ],
#     "auth": "3a82ae7bbdaf007210ff8d6c6673b218",
#     "id": 1
# }

########################################
#### 获取Template OS Linux模板ID
####参考 https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/template/get
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "3a82ae7bbdaf007210ff8d6c6673b218",
#     "id": 1
# }

###########################################
###### 创建主机nsd1903web1，加入Linux servers组，应用Template OS Linux模板
### 创建主机 https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/host/create
### 查询groupid https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/hostgroup/get
###查询到的groupid 才能填写在 创建主机的模板中,,, 取web页面上查询 主机信息
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.24",
                "dns": "",
                "port": "10050"   ####zabbix_agent 的端口
            }
        ],
        "groups": [
            {
                "groupid": "2"        ####通过 hostgroup.get 查询
            }
        ],
        "templates": [
            {
                "templateid": "10001"  #####通过 template.get 查询
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },

    "auth": "3a82ae7bbdaf007210ff8d6c6673b218",
    "id": 1
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())