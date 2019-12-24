import os
import time
import datetime
def function_file(path):
    move_list = []  # 创建一个空列表
    if os.path.exists(path):  # 判断文件目录是否存在,若存在就往下执行
        for root, dirs, files in os.walk(path):
            for file in files:
                a = os.path.join(root, file)
                b = time.localtime(os.stat(a).st_ctime)  # 取文件创建日期
                b = time.strftime("%Y%m%d", b)  # 把取到的文件创建日期格式化,格式:20191223
                b = int(b)  # 把取到的文件日期改成int类型
                today = datetime.datetime.today().date()  # 取当前日期,格式:2019-12-24
                offset = today + datetime.timedelta(days=-30)  # 取前7天的日期,用当前日期加上-7就是求往后推7天的日期
                offset = str(offset)  # 把日期转换成字符串,格式:2019-12-24
                offset = int(offset.replace('-', ''))  # 把日期格式中间的横杠去掉,然后在转换成int类型
                if b < offset:  # 如果文件的创建日期小于指定的日期,就执行下面删除的动作                
                    move_list.append(a)  # 把删除的文件添加到列表当中
                    os.remove(a)
                else:
                    pass
    else:
        print("文件目录不存在")
    print("已清除如下文件:")
    for i in move_list:
        print(i)
    time.sleep(5)

function_file("D:\\IISProject\\CLZ.Client\\logs")
function_file("D:\\IISProject\\CLZ.Client.Test\\logs")
function_file("D:\\IISProject\\CLZ-Release\\logs")
function_file("D:\\IISProject\\CLZ-Release-Api\\logs")
function_file("D:\\IISProject\\CLZ-Test\\logs")
function_file("D:\\IISProject\\CLZ-Test-Api\\logs")
function_file("D:\\IISProject\\NewPosServer\\pos_logs")
function_file("D:\\IISProject\\NewPosServer\\version")
function_file("D:\\IISProject\\NewPosServer\\logs")
function_file("D:\\IISProject\\NewPosServer.Test\\version")
function_file("D:\\IISProject\\NewPosServer.Test\logs")
function_file("D:\IISProject\Pay-Release\PayLogger\LogManager")
function_file("D:\\IISProject\\Pay-Release\\PayLogger\\UserManager")
function_file("D:\\IISProject\\Pay-Test\\PayLogger\\LogManager")
function_file("D:\\IISProject\\Pay-Test\\PayLogger\\UserManager")
