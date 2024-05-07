# 通过占位的形式完成拼接
name = "world"
print("hello, %s" % name)

# 通过占位的形式完成数字和字符串的拼接
age_num = 23
name_num = 0o07
format_str = "我是 %s ,今年 %s 岁" % (name_num, age_num)
print(format_str)

# 宽度限制
num1 = 11
num2 = 11.345

print("num 11 limit width 5 : %5d" % num1)
print("num 11 limit width 1 : %1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345不限制，小数精度2，结果是：%.2f" % num2)