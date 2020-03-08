
#按照教程上的学习,代码还是运行报错,后面在来学习
"""
这里以"植物大战僵尸"游戏为案例,我们在玩游戏时,生命力是100,那么在打僵尸的时候会牺牲生命力(也就是
僵尸对人生的伤害),当生命力等于某个值的时候,自动将生命力还原为100;
"""
import win32process #进程模块
import win32con  #系统定义
import win32api  #调用系统模块
import ctypes   #C语言类型
import win32gui  #界面

#解释:定义一个PROCESS_ALL_ACCESS常量,用这个常量标识,以最高权限打开一个进程
PROCESS_ALL_ACCESS =(0x000F0000|0x00100000|0xFFF) #| 位运算符,0x十六进制


"""
解释:创建一个窗体标识:windows,FindWindow表示查找一个窗体,它有两个参数("类名","标题"),
这里可以用spy软件
"""来查找"类名"与"标题"
window=win32gui.FindWindow("343434","Plants vs. Zombies 1.2.0.1073 RELEASE")


"""
pid为所运行软件的进程,我们可以在window系统任务管理器中看到所运行的程序的pid(进程编号)
GetWindowThreadProcessId(window):表示根据窗体抓取进程编号
"""
hid,pid=win32process.GetWindowThreadProcessId(window)


"""
OpenProcess(PROCESS_ALL_ACCESS,False,pid):表示用最高权限打开进程编号
"""
phand=win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)


"""
ctypes.c_long():表示以C语言的整数类型读取数据
"""
date=ctypes.c_long()


#加载内核模块:kernel32
mydll = ctypes.windll.loadLibrary("c:\\windows\\System32\\kernel32.dll")

#首先把phand转换成int类型,然后读取内存地址
mydll.ReadProcessMemory(int(phand),546813992,ctypes.byref(date),4,None)


print(date.value)

