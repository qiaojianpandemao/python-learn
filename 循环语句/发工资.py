import random

balance = 10000

for index in range(21):
    # 判断账户余额是否充足
    if balance == 0:
        print("公司账户余额不足,发不出工资来了")
        break
    # 随机生成绩效
    performance = random.randint(0,10)
    if performance >=5:
        balance -= 1000
        print(f"给员工{index} 发放工资 1000 元成功,账户余额 {balance} 元")