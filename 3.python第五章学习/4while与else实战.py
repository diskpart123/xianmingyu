# while与else实战
import win32com.client

a = win32com.client.Dispatch("SAPI.SPVOICE")
num = 0
while num < 7:  # 如果i等于7或者大于7时,跳出while循环,执行else代码块
    print("while", num)
    a.Speak("吴浩然的女神有" + str(num) + "个备胎")
    num += 1
else:
    print("else", num)
    a.Speak("吴浩然的女神有" + str(num) + "个备胎,够了,有点忙不过来了")
