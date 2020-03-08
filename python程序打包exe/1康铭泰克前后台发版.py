

import os
import shutil
import zipfile
import time
temp = "康铭泰克前后台发布系统"
print(temp.center(50, "*"))

count = 0
while count < 5:
    count += 1
    path = input("请输入升级临时文件目录:")
    sele_path = os.listdir(path)
    refer_to = input("输入文件名称:")
    for i in sele_path:
        if refer_to in i:
            print(i)
            path = path + "\\" + i
            print(path)
            break

    status = int(input("请输入状态码:1(pos),2(Mis_Bin),3(Mis_Release),4(Pay_Bin),5(NewPosServer):"))

    if status == 1:
        print("把pos升级包拷贝到E:\IISProject\CLZ-Test\PosVer")
        zhantie_mubiaolujing = input("目标路径:")
        if refer_to in path:
            shutil.copy(path, zhantie_mubiaolujing)  # 把原路径(fuzhi_yuanlujing)的文件复制到目标路径(zhantie_mubiaolujing)
        else:
            print("不包含:", refer_to)
    elif status == 2:
        print("把Mis_Bin升级包拷贝到E:\IISProject\CLZ-Test\\bin")
        zhantie_mubiaolujing = input("目标路径:")
        if refer_to in path:
            shutil.copy(path, zhantie_mubiaolujing)
            # yuanlujing = input("Mis_Bin源路径(需要把压缩文件的后缀带上,如(.zip)):")
        else:
            print("不包含:", refer_to)
        if refer_to in path:
            z = zipfile.ZipFile(path, "r")  # 读取压缩文件
            jieya_address = input("解压地址:")
            z.extractall(jieya_address)  # 解压地址
            time.sleep(5)
            z.close()
        else:
            print("不包含:", refer_to)


    elif status == 3:

        print("把Mis_Release升级包拷贝到E:\IISProject\CLZ-Test.Publish下")
        zhantie_mubiaolujing = input("目标路径:")
        if refer_to in path:
            shutil.copy(path, zhantie_mubiaolujing)
        else:
            print("不包含:", refer_to)
        if refer_to in path:
            z = zipfile.ZipFile(path, "r")  # 读取压缩文件
            jieya_address = input("解压地址:")
            z.extractall(jieya_address)  # 解压地址
            time.sleep(5)
            z.close()

        else:
            print("不包含:", refer_to)


    elif status == 4:
        print("把Pay_Bin升级包拷贝到E:\IISProject\Pay-Test\\bin下")
        zhantie_mubiaolujing = input("目标路径:")
        if refer_to in path:
            shutil.copy(path, zhantie_mubiaolujing)
        else:
            print("不包含:", refer_to)
        if refer_to in path:
            z = zipfile.ZipFile(path, "r")  # 读取压缩文件
            jieya_address = input("解压地址:")
            z.extractall(jieya_address)  # 解压地址
            time.sleep(5)
            z.close()
        else:
            print("不包含:", refer_to)

    elif status == 5:
        print("把PosServer升级包拷贝到E:\IISProject\\NewPosServer.Test下")
        zhantie_mubiaolujing = input("目标路径:")
        if refer_to in path:
            shutil.copy(path, zhantie_mubiaolujing)
        else:
            print("不包含:", refer_to)
        if refer_to in path:
            z = zipfile.ZipFile(path, "r")  # 读取压缩文件
            jieya_address = input("解压地址:")
            z.extractall(jieya_address)  # 解压地址
            time.sleep(5)
            z.close()
        else:
            print("不包含:", refer_to)
