# 计算1970年到2019年，有多少小时、多少天、多少年

import time

timedata = time.time()
timedata = int(timedata)  # 取整数，多少秒

hour = (timedata / 3600)  # 1小时有3600秒，所以除以3600

today = (timedata / 3600 / 24)  # 用计算出的小时数在除以24(一天有24小时)，算出多少天

year = (timedata / 3600 / 24 / 365)  # 用计算出的天数在除以365(一年有365天)，算出多少年

print(hour)
print(today)
print(year)
