# -*- coding: utf-8 -*-
# @Time    : 2020/01/23 17:36
# @Author  : xianming yu
# @File    : test1.py

class Dog():
    def cat(self):
        print("This is cat!")
    def shopping(self):
        print("This is shopping!")

s1=Dog()
print(id(Dog))
print(id(s1))
s1.cat()
s1.shopping()
s2=s1
print(dir(s1))
print(id(s2))
