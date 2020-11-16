# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:35:53 2018

@author: nitingera
"""

count=0
sum=0

while (count <20):
    while(sum < 5):
        print("sum is", sum)
        sum += 1
    count += 1
    print("count is", count)

dt_group=["Deepika", "Kranti", "Rupesh", "Nitin", "Devesh", "Neha", "Anu"]

for name1 in dt_group:
    x = 0
    while(x < 5):
        print(name1)
        x += 1

name="My name is Nitin Gera"

for letter in name:
    if letter == " ":
        continue
    
    if letter == "t":
        break
    
    print("letter is", letter)
    
print("End of program")
        