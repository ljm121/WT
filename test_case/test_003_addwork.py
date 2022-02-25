# -*- coding: utf-8 -*-
# @Time    : 2022/2/25 13:41
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : test_003_addwork.py
# @Software: PyCharm
import time
from public.pages.base_element_method import Base_Element_Method as BEM
from public.pages.page_element import Page_Element as PE
from selenium import webdriver
from public.utils.login_data import Login_Data
from selenium.webdriver.common.action_chains import ActionChains
from public.utils.logger import trace_log

url_value = Login_Data().get_url()
user_value = Login_Data().get_user()
pwd_value = str(Login_Data().get_password())


class Test_AddWork(BEM):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        BEM.set_driver(cls.driver)
        driver = BEM.get_driver()
        driver.get(url_value)
        elemt = BEM.find_element(PE.user_elemt)
        BEM.send_keys(elemt, user_value)
        elemt = BEM.find_element(PE.pwd_elemt)
        BEM.send_keys(elemt, pwd_value)
        elemt = BEM.find_element(PE.click_login)
        BEM.get_click(elemt)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        BEM.sleep(5)
        BEM.set_driver(cls.driver.quit())

    @trace_log
    def test_003_addwork(self,):
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_xpath('//*[text()="排班管理"]')
        ActionChains(self.driver).move_to_element(elem).perform()
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_xpath('//*[text()="快速排班"]')
        BEM.get_click(elem)
        elem = self.driver.find_element_by_xpath('//*[text()="按人员排班"]')
        BEM.get_click(elem)
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        title = self.driver.title
        # print(title)
        self.assertEqual(title, "排班", "页面title属性值错误！")

        # ActionChains.drag_and_drop(start_elem, end_elem).perform()
        # BEM.sleep(2)
        elem = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[1]/div/form/div['
                                                 '4]/div/div/div/div/div/input')
        BEM.get_click(elem)
        elem = self.driver.find_element_by_xpath('//*[text()="4月"]')
        BEM.get_click(elem)
        time.sleep(5)
        # elem = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div/form')
        # BEM.get_click(elem)

        # start_elem = self.driver.find_element_by_xpath('//*[text()="20-21"]')
        # end_elem = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[3]/div/div/div/div['
        #                                              '2]/div/div[1]/div[3]/div[2]/div[20]')
        # ActionChains(self.driver).drag_and_drop(start_elem, end_elem).perform()
