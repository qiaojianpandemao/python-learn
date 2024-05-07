money = 5000000


# 函数定义
# 查询余额函数
def select_money():
    print("你的余额为: %d" % money)
    print_menu()


# 取款函数
def withdrawal():
    fee = input("请输入取款金额:")
    global money
    money = money - int(fee)
    print("取款成功,你的余额为: %d" % money)
    print_menu()


# 存款函数
def add_money():
    fee = input("请输入存款金额:")
    global money
    money += int(fee)
    print("存款成功,你的余额为: %d" % money)
    print_menu()


# 主菜单函数
def print_menu():
    print("1------查询余额")
    print("2------存款")
    print("3------取款")
    print("4------主菜单")


name = input("please input your name:")
print_menu()
while True:
    operation = input("请输入你的操作:")
    if operation == "1":
        select_money()
    elif operation == "2":
        add_money()
    elif operation == "3":
        withdrawal()
    else:
        print("非法输入!!!")
        break
