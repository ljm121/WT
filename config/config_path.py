# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 13:59
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : config_path.py
# @Software: PyCharm
import os

project_path = r'C:\pycharm\WT'

# data数据路径
data_path = os.path.join(project_path, 'data')

# 公共页面数据
pages_path = os.path.join(project_path, 'public', 'pages')

# 工具类的路径
utils_path = os.path.join(project_path, 'public', 'utils')

# 报告路径
report_path = os.path.join(project_path, 'report')

# 日志路径
log_path = os.path.join(project_path, 'test_log')

# 用例路径
case_path = os.path.join(project_path, 'test_case')
