# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 17:01
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : login_token.py
# @Software: PyCharm

from login_data import Login_Data
import requests
import getpass
import json


def Login_Token():
    """获取登录后的token"""
    login_data = Login_Data()
    headers = {'Content-Type': 'application/json'}
    url = "https://gateway.woketest1.com/basic/login/loginUser"
    data = {
        "account": login_data.get_user(),
        "password": getpass.getpass(login_data.get_password())
    }
    print(data)
    # print(json.dumps(data))
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response.text)
    print(response.status_code)
    print(response.json()["data"]["token"])
    return response.json()["token"]
    # 返回JSON中data数据的token
    # return print(response.json()['data']['token'])


if __name__ == '__main__':
    Login_Token()
