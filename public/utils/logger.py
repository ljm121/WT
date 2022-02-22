# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 14:19
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : logger.py
# @Software: PyCharm
import logging
import time
from config.config_path import log_path


class Logger:
    def __init__(self):
        log_folder = log_path
        now_time = time.strftime('%Y_%m_%d')
        self.log = log_folder + '\\' + now_time + '.log'
        # print(self.log)
        self.stdout_format = '%(asctime)s - %(levelname)s : %(message)s'

        # log_name = time.strftime('%Y-%m-%d', time.localtime()) + '.log'
        # check_folder_exists = lambda folder: os.path.exists(folder)
        # if not check_folder_exists(log_folder):
        #     os.makedirs(name=log_folder, exist_ok=True)
        # self.stdout_format = '%(asctime)s - %(levelname)s : %(message)s'
        # self.log = os.path.abspath(os.path.join(log_folder, log_name))

    def logger(self):
        # 设置日志输出格式
        formatter = logging.Formatter(self.stdout_format)
        # 设置控制台日志
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        # 设置文件日志
        file_handler = logging.FileHandler(filename=self.log, encoding='utf-8')
        file_handler.setFormatter(formatter)
        # file_handler.setLevel(logging.INFO)
        logging.getLogger().addHandler(console)
        logging.getLogger().addHandler(file_handler)
        logging.getLogger().setLevel("INFO")
        return logging.getLogger()


log = Logger().logger()


def trace_log(func):
    def wrapper(*args, **kwargs):
        log.info('Function:[{}], args:{}, kwargs:{}'.format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        log.info('Function:[{}], Result: {}'.format(func.__name__, result))
        return result

    return wrapper


# if __name__ == '__main__':
#     """调试代码"""
#
#
#     @trace_log
#     def add(a, b):
#         return a + b
#
#
#     add(1, 2)