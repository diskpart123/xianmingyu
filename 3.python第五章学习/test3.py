
""""
处理excel表格数据

import openpyxl
from openpyxl.styles import Alignment

wb = openpyxl.load_workbook("example.xlsx")  # 打开工作簿
sheet1=wb["Sheet1"]

print("{}*{}".format(sheet1.max_row,sheet1.max_column))

for row in sheet1.iter_rows(min_row=1,max_col=24): #表示取3列中每一行的数据,也就是一个数据区间
    for cell in row:
        cell_new=str(cell.value)
        print(format(cell_new, "19s"), end=" ")
        # print(cell.value,end=" ")
    print()
"""
"""
文件清理定时任务


from threading import Timer
import datetime
# 每隔两秒执行一次任务
def printHello():
    print('TimeNow:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    t = Timer(10, printHello)
    t.start()

if __name__ == "__main__":
    printHello()
"""
"""
import  os
import time
import datetime
path=input("需要清除文件的目录:")
sele_path=os.listdir(path)
for i in sele_path:
    a=path+"\\"+i
    b=time.localtime(os.stat(a).st_ctime)
    b=time.strftime("%Y%m%d",b)
    # print(b)
    today = datetime.datetime.now()
    offset = datetime.timedelta(days=-3)
    re_date = (today + offset).strftime('%Y%m%d')
    if re_date>b:
        os.remove(a)
    else:
        pass
    # print(i,time.ctime(os.stat(path+"\\"+i).st_ctime) )#文件的创建时间

"""
"""
import datetime
today = datetime.datetime.now()
offset = datetime.timedelta(days=3)
re_date = (today + offset).strftime('%Y%m%d')
today=today.strftime('%Y%m%d')
print("re_date:",re_date)
print(today)
print(re_date)
print(today>re_date)
"""







