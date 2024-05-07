"""
演示Python的input语句
获取键盘的输入信息
"""
name = input("请告诉我你是谁？")
print("我知道了，你是:%s" % name)

# 输入数字类型
num = input("请告诉我你的银行卡密码：")
# 数据类型转换
num = int(num)
print("你的银行卡密码的类型是：", type(num))

name = """黑马程序员"""
eat = input("你猜我今天吃了什么?")
print("我知道了,我也很喜欢吃 %s" % eat)