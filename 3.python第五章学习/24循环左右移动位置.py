import win32gui
import win32con
import  time
qq=win32gui.FindWindow("TXGuiFoundation","QQ")
for size in range(0,800,10):   #如果让放大速度慢一点,可以把步长10,改成1
    win32gui.SetWindowPos(qq,  #操作qq
                          win32con.HWND_TOPMOST, #最上方
                          size, #位置x
                          0, #位置y
                          300,#长度
                          300,#宽度
                          win32con.SWP_SHOWWINDOW
                          )
    for size in range(800,0,-10): #如果让缩小速度慢一点,可以把步长-10,改成-1
        win32gui.SetWindowPos(qq,  #操作qq
                              win32con.HWND_TOPMOST, #最上方
                              size, #位置x
                              0, #位置y
                              300,#长度
                              300,#宽度
                              win32con.SWP_SHOWWINDOW
                              )

