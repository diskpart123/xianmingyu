# while与else
import win32com.client

a = win32com.client.Dispatch("SAPI.SPVOICE")
i = 1  # i用来记录次数的
while i < 5:  # 如果i等于5或者大于5时while停止执行,此时代码就会跳转到else代码块中,执行else下面的语句
    print(i)
    a.Speak("我爱你中国" + "这是第" + str(i) + "次")
    i += 1  # 每循环一次i+1
else:  # 如果i等于5或者大于5时执行else代码块语句
    print("go", i)
    a.Speak("我都说了" + str(i - 1) + "次了,足以表示我对祖国的热爱!")
