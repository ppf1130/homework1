#!/usr/bin/env python
# -*- coding: utf-8 -*-

import money

# 定义工资数值变量
salary = 1000

# 定义查询工资方法
def select_money():
    if money.send_salary == True:
        print(f"发了{salary}元工资")
        return salary
    else:
        print("还没有发工资呐")
        return 0
