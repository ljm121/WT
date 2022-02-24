# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 16:28
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : test_002_adduser.py
# @Software: PyCharm
import time


from public.utils.prtsc import Bug_Screen as B_S
from public.pages.base_element_method import Base_Element_Method as BEM
from public.pages.page_element import Page_Element as PE
from selenium import webdriver
from public.utils.login_data import Login_Data
from selenium.webdriver.common.action_chains import ActionChains
from public.utils.logger import trace_log


url_value = Login_Data().get_url()
user_value = Login_Data().get_user()
pwd_value = str(Login_Data().get_password())


class Test_AddUser(BEM):
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
    def test_002_adduser(self):
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_xpath('//*[text()="组织和人员"]')
        ActionChains(self.driver).move_to_element(elem).perform()
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_xpath('//*[text()="人员管理"]')
        ActionChains(self.driver).move_to_element(elem).perform()
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_xpath('//*[text()="在职人员管理"]')
        BEM.get_click(elem)
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_xpath('//*[text()="新增员工"]')
        # elem = self.driver.find_element_by_xpath('//*[@id="rootLayoutContent"]/div/div/div/div/div[2]/div/div[1]/div['
        #                                          '2]/div/div[2]/div/button/span')
        BEM.get_click(elem)
        BEM.sleep(5)
        elem = self.driver.find_element_by_id("staff_surname")
        # elem = self.driver.find_element_by_xpath('/html/body/div/section/main/div/div/div/div/div[2]/div/div['
        #                                          '3]/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div['
        #                                          '1]/div/input')
        BEM.send_keys(elem, '测试')
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_id("staff_name")
        BEM.send_keys(elem, 'UI')
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_id("staff_account")
        BEM.send_keys(elem, 13237020055)
        elem = self.driver.find_element_by_xpath('//*[text()="固定工时"]')
        BEM.get_click(elem)
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_xpath('//*[text()="排班考勤"]')
        BEM.get_click(elem)
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_xpath('/html/body/div/section/main/div/div/div/div/div[2]/div/div['
                                                 '3]/div/div/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div/div['
                                                 '2]/div/div[3]/div[2]/div[1]/div/div/div[2]/div[1]/span[1]/input')
        BEM.get_click(elem)
        elem = self.driver.find_element_by_xpath('//*[text()="默认考勤组(排班考勤)"]')
        BEM.get_click(elem)

        # js = "window.scrollTo(0,document.body.scrollHeight)"
        # self.driver.execute_script(js)
        # elem = self.driver.find_element_by_xpath('/html/body/div/section/main/div/div/div/div/div[2]/div/div['
        #                                          '3]/div/div/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div/div['
        #                                          '2]/div/div[9]/div[2]/div[2]/button/span')
        # BEM.get_click(elem)
        # BEM.sleep(10)
        elem = self.driver.find_element_by_xpath('/html/body/div/section/main/div/div/div/div/div[2]/div/div['
                                                 '3]/div/div/div[2]/div/div/div[3]/div/button[2]')
        BEM.get_click(elem)
        time.sleep(5)
        self.driver.save_screenshot('use.png')
