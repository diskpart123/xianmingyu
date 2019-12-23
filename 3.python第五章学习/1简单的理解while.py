# while 規則与if一样,在执行时会把表达式自动转换成bool类型
# True:继续循环(1,2,-1," ",True,1.234),括号中代表的都为True
# False:退出循环(0,"",None,False),括号中代表的都为False
import win32com.client

a = win32com.client.Dispatch("SAPI.SPVOICE")
count = True
while " ":
    a.Speak("测试")
