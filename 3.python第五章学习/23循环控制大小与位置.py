import win32gui
import win32con
import  time
notepad=win32gui.FindWindow("Notepad","新建文本文档 - 记事本")

for i in range(4):   #次数限制:共放大和缩小4次

    for size in range(0,800,10):   #如果让放大速度慢一点,可以把步长10,改成1
        win32gui.SetWindowPos(notepad,  #操作记事本
                              win32con.HWND_TOPMOST, #最上方
                              0, #位置x
                              0, #位置y
                              size,#长度
                              size,#宽度
                              win32con.SWP_SHOWWINDOW
                              )
    for size in range(800,0,-10): #如果让缩小速度慢一点,可以把步长-10,改成-1
        win32gui.SetWindowPos(notepad,  #操作记事本
                              win32con.HWND_TOPMOST, #最上方
                              0, #位置x
                              0, #位置y
                              size,#长度
                              size,#宽度
                              win32con.SWP_SHOWWINDOW
                              )

