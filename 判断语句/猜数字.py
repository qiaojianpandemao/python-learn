import random

rand_num = random.randint(1, 10)
print(rand_num)
input_num = input("请输入一个数字(1-10):")

if int(input_num) == rand_num:
    print("你猜对了")
else:
    if int(input_num) > rand_num:
        print("你输入的数字大了")
    else:
        print("你输入的数字小了")

    input_num = input("请输入一个数字(1-10):")

    if int(input_num) == rand_num:
        print("你猜对了")
    else:
        if int(input_num) > rand_num:
            print("你输入的数字大了")
        else:
            print("你输入的数字小了")

        input_num = input("请输入一个数字(1-10)")

        if int(input_num) == rand_num:
            print("你猜对了")
        elif int(input_num) > rand_num:
            print("你输入的数字大了")
        else:
            print("你输入的数字小了")


