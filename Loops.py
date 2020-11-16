# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:23:17 2018

@author: nitingera
"""

x = 1

print("----------")
while (x < 25):
    print("x = ", x)
    x += 1
else:
    print("x is no longer less than 25")
print("End of program")

name="My name is Nitin Gera"

for alphabet in name:
    print("Letter is:", alphabet)

dt_group=["Deepika", "Kranti", "Rupesh", "Nitin", "Devesh", "Neha", "Anu"]

for employee in dt_group:
    print("employee name:", employee)