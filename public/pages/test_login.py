# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 15:57
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : test_login.py
# @Software: PyCharm
import time
import unittest
from selenium import webdriver
from public.pages.base_element_method import Base_Element_Method as BEM  # 定位方法的类
from public.pages.page_element import Page_Element as PE  # 登录用的元素
from public.utils.logger import trace_log
from public.utils.login_data import Login_Data

url_value = Login_Data().get_url()
user_value = Login_Data().get_user()
pwd_value = str(Login_Data().get_password())


class Test_Login(BEM):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        BEM.set_driver(cls.driver)

    @classmethod
    def tearDownClass(cls):
        BEM.sleep(5)
        BEM.set_driver(cls.driver.quit())

    @trace_log
    def test_001_login(self):
        driver = BEM.get_driver()
        driver.get(url_value)

        elemt = BEM.find_element(PE.user_elemt)
        BEM.send_keys(elemt, user_value)

        elemt = BEM.find_element(PE.pwd_elemt)
        BEM.send_keys(elemt, pwd_value)

        elemt = BEM.find_element(PE.click_login)
        BEM.get_click(elemt)
        # driver.quit()
        # print(BEM.get_title())
        # self.assertEqual(BEM.get_title(), '工作台', msg='断言成功，内容相等')
        # BEM.sleep(2)
        # return BEM.get_title()

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
