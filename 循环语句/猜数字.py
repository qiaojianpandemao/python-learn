import random

rand_num = random.randint(1, 10)

# 计数器
count = 0

# 循环结束工具
flag = True
while flag:
    input_num = input("请输入一个数字(1-10):")
    if rand_num == int(input_num):
        flag = False
        print("你猜对了!!!")
    elif rand_num < int(input_num):
        print("大了")
    else:
        print("小了")
    count += 1
print(f"你总共猜了 {count} 次")
