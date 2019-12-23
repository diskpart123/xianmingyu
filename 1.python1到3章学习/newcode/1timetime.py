import time

"""
mytime = time.time()

print(mytime)  # 这里计算的是:从1970年到现在的时间

second = int(mytime)  # 一共的秒数
print("自从1970年过去了%d秒" % second)

seconds = second % 60  # 剩余的秒数
print("剩余的秒数为:%d" % seconds)

hours = int(mytime) // 3600  # 过去了多少小时
print("过去了%d小时" % hours)

mins = (int(mytime) - int(mytime) // 3600 * 3600)
print(mins)
mins = (mins - seconds) // 60
print("过去了%d分钟" % mins)

print("自从1970年到现在过去了%d小时%d分%d秒" % (hours, mins, seconds))
"""




# 案例：求过去了%d天,%d小时,%d分钟,%d秒
"""
miaoshu = 129600

# 求剩余的秒数

shengyumiaoshu = miaoshu % 60
print("剩余秒数是:%d" % shengyumiaoshu)

# 求小时数

xiaoshi = miaoshu // 3600

print("小时数是:%d" % xiaoshi)

fenzhong = (int(miaoshu) - int(miaoshu) // 3600 * 3600)
print("分钟数是:%d" % fenzhong)

fenzhong = (fenzhong - shengyumiaoshu) // 60
print("过去了%d分钟" % fenzhong)

tianshu = xiaoshi // 24

xiaoshi = xiaoshi % 24

print("基于129600秒过后过去了%d天数,%d小时,%d分钟,%d秒" % (tianshu, xiaoshi, fenzhong, shengyumiaoshu))
"""