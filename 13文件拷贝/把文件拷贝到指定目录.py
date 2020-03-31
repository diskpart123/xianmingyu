
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 15:00
# @Author  : xianming yu
# @File    : 把文件拷贝到指定目录.py

import os
import shutil

def get_all_path(open_file_path):
    rootdir = open_file_path
    path_list = []
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        com_path = os.path.join(rootdir, list[i])
        #print(com_path)
        if os.path.isfile(com_path):
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path))
    return path_list

test=get_all_path("E:\\python3高级视频\\667501933")
for i in test:
    if i.endswith(".flv"):
        # 把文件拷贝到 E:\\python3高级视频\\ceshi1目录下
        shutil.copy(i, "E:\\python3高级视频\\ceshi1")