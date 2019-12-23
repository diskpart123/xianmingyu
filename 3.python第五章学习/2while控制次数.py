# while循环控制次数

import win32com.client

a = win32com.client.Dispatch("SAPI.SPVOICE")
i = 0  # i用来记录次数的
while i < 5:  # 如果i等于5或者大于5时while停止执行
    print(i)
    a.Speak("我爱你中国"+"这是第"+str(i+1)+"次")
    i += 1  # 每循环一次i+1
