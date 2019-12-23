"""
比喻说大家借高利贷，借10000元，月利率是1.05%，那么最终1年需要还多少钱呢？
首先知道月利率后我们把年利率求出来：年利率=月利率的12次方=0.0105的12次方=1.7958
1年还款金额=1.7958‬*10000=17958


中国增长率为1.065%，那么10年后中国的增长率为0.01065的10次方=1.877
"""


daikuanshu = eval(input("请输入贷款金额>:"))
nianlilv = eval(input("请输入年利率>:"))  # 商贷的年利率是4.9%转换成小数就是0.049,所以这里的输入的时候我们输入0.049,不要输入4.9
yuelilv = nianlilv / 12  # 用年利率除以12得到每个月的月利率
nianxian = eval(input("请输入贷款年限>:"))
yuegong = (daikuanshu * yuelilv) / (1 - 1 / (1 + yuelilv) ** (nianxian * 12))

zonghuankuanshu = yuegong * nianxian * 12
print("月供金额为", yuegong)
print("总还款额", zonghuankuanshu)
