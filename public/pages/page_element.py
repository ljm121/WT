# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 14:09
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : page_element.py
# @Software: PyCharm
'''
存放页面元素
'''


class Page_Element():
    # 登录
    user_elemt = ('xpath', '//*[@id="AccountLogin_account"]/input')
    pwd_elemt = ('xpath', '//*[@id="AccountLogin_password"]/input')
    click_login = ('xpath', '//*[@id="AccountLogin"]/div[5]/div/div/div/div/button/span')

    # 忘记密码
    set_elemt = ('xpath', '//*[@id="AccountLogin"]/a')

    # 注册
    zhuce = ('xpath', '//*[@id="AccountLogin"]/div[5]/div/div/div/div/a/button/span')
