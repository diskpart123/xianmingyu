# print(not True)  # False
# print(not False)  # True
# print(not not True)  # True
# print(not not False)  # False

genders = True
if not genders: # False
    print("girl")
else:
    print("boy")


genders = True
if not not genders: #True
    print("girl")
else:
    print("boy")
"""
总结:
    逻辑运算符not的结合性是:从右往左
    加减乘除的结合性是:从左往右
"""
