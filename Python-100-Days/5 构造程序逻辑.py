"""
找出所有水仙花数
"""

array = list(range(10))  # 未知数组创建
a = 0
for i in range(100, 1000):
    g = i % 10
    s = i // 10 % 10
    b = i // 100
    if g ** 3 + s ** 3 + b ** 3 == i:
        array[a] = i
        a += 1
for i in range(a):
    print(array[i])

"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
"""
import time
from random import randint


def delay():
    print("正在投掷骰子...")
    time.sleep(2)


def main():
    money = 1000
    print("你现在的赌注为%d" % money)
    while money > 0:
        debt = int(input("请下注："))
        if debt < 0 or debt > money:
            break
        # need_go_on = False
        first = randint(1, 6) + randint(1, 6)
        delay()
        print("第1次的结果是%d" % first)
        if first == 7 or first == 11:
            money += debt
            print("玩家胜,你现在的赌注为%d" % money)
            continue
        elif first == 2 or first == 3 or first == 12:
            money -= debt
            print("庄家胜,你现在的赌注为%d" % money)
            continue
        # else:
        # need_go_on = True
        else:
            flag = 2
            while True:
                after = randint(1, 6) + randint(1, 6)
                delay()
                print("第%d次的结果是%d" % (flag, after))
                flag += 1
                if after == first:
                    money += debt
                    print("玩家胜,你现在的赌注为%d" % money)
                    break
                if after == 7:
                    money -= debt
                    print("庄家胜,你现在的赌注为%d" % money)
                    break
    print("你破产了")


if __name__ == main():
    main()

'''
1. 生成**斐波那契数列**的前20个数。
'''
# 我的答案
import numpy as np

a = np.zeros(20).astype(int)
a[0] = 1
a[1] = 1
for i in range(1, 19):
    a[i + 1] = a[i - 1] + a[i]
print(a)

# 标准答案
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')

"""
找出10000以内的完美数。
"""

sum_ = 0
for i in range(1, 10000):
    for a in range(1, i):
        if i % a == 0:
            sum_ = sum_ + a
    if sum_ == i:
        print(i)
    sum_ = 0

