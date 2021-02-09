#!/usr/bin/env python
# -*- coding: utf-8 -*-

import money
from sendmoney.send_money import send_money
from sendmoney.select_money import select_money

if __name__ == '__main__':
    send_money()
    salary = select_money()
    money.saved_money = money.saved_money + salary
    print(f"我现在有存款{money.saved_money}元了！")