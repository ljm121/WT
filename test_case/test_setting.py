# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 16:28
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : test_setting.py
# @Software: PyCharm
from public.pages.base_element_method import Base_Element_Method as BEM
from public.pages.page_element import Page_Element as PE


class Test_Setting(BEM):
    @classmethod
    def setUpClass(cls):
        BEM.sleep(2)

    @classmethod
    def tearDownClass(cls):
        BEM.sleep(3)
        BEM.close()

    # def test_002_setting(self):
    #     elem = BEM.find_element(PE.zhuce)
    #     BEM.get_click(elem)
