# 在使用文字转语音之前需要在pycharm中安装pywin32的库

import win32com.client  # 导入系统客户端包

speaker = win32com.client.Dispatch("SAPI.SPVOICE")  # 调用系统接口
a = """
　　最后，再次感谢学校党委、行政和各院、部、处的领导长期以来对学生创业超市的
关心和支持，我们创业超市全体员工祝愿西南科技大学的明天更美好，祝愿各级领导身
体健康，工作顺利。祝愿全校学友学业有成，前程似锦！
　　谢谢！
"""
speaker.Speak(a)
speaker.Speak("谊品生鲜 AB0001 大仓")

