# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 14:20
# @Author  : Ljm
# @Email   : lijm@woketech.com
# @File    : read_excel.py
# @Software: PyCharm
import os
import xlrd
from config.config_path import data_path


class Read_Excel():
    def __init__(self, data, num):
        self.Data_path = os.path.join(data_path, data)  # 合并data文件的路径
        self.open_excel = xlrd.open_workbook(self.Data_path)  # 打开Excel文件
        self.sheet = self.open_excel.sheet_by_index(num)

    def read_value(self, rows, cols):
        cell_va = self.sheet.cell_value(rows, cols)  # 调用cell_value方法，传入单元格的行和列
        return cell_va


if __name__ == '__main__':
    read_excel = Read_Excel('Data.xlsx', 0)
    print(read_excel.read_value(1, 0))
