# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 16:17
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : run_test.py
# @Software: PyCharm
import time
import unittest

# 把报告路径和项目路径导入（项目路径需要作为批量执行用例的路径）
from config.config_path import report_path, project_path
from public.utils.HTMLTestRunner import HTMLTestRunner
from public.utils.mail_new import Maile_test


def aout_run():
    new_report_path = report_path + '\\' + time.strftime('%Y_%m_%d_%H_%M_%S') + '_ui_report.html'
    disc = unittest.defaultTestLoader.discover(project_path, 'test_*.py')
    with open(new_report_path, 'wb') as file_wb:
        runner = HTMLTestRunner(stream=file_wb, title='class_UI_report', description='报告如下', verbosity=2)
        runner.run(disc)

        # 发送邮件
        email = Maile_test(new_report_path)
        email.send_mail()


aout_run()
