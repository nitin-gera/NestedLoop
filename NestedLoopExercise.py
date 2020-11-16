# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:57:41 2018

@author: nitingera
"""

balance = 2250
interestRate = .045
term = 120

curr_month = 1

while(curr_month <= term):
    interest = balance * interestRate/12
    balance += interest
    print("current month:%d interest:%.2f balance:%.2f"%(curr_month, interest, balance))
    curr_month += 1