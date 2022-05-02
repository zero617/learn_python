"""
输入一个正整数判断它是不是素数
"""
from math import sqrt

number = int(input("请输入一个正整数："))
p = int(sqrt(number))
flag = True
for i in range(2, p + 1):
    if number % i == 0:
        flag = False
        break
if flag and number != 1:
    print("%d是素数" % number)
else:
    print("%d不是素数" % number)

"""
输入两个正整数计算它们的最大公约数和最小公倍数
"""
a = int(input("请输入a:"))
b = int(input("请输入b:"))
if a > b:
    n = a
else:
    n = b
for i in range(n, 0, -1):
    if a % i == 0 and b % i == 0:
        print("%d是最大公约数" % i)
        print("%d是最小公倍数" % (a * b // i))
        break

"""
打印三角形图案
"""
# 自己写的
n = int(input("请输入行数:"))

for a in range(n):
    for i in range(a + 1):
        print('*', end='')
    print('')

print('')

for a in range(n):
    for i in range(n - a - 1):
        print(' ', end='')
    for i in range(a + 1):
        print('*', end='')
    print('')

print('')

for a in range(n):
    for i in range(n - a - 1):
        print(' ', end='')
    for i in range((a + 1) * 2 - 1):
        print('*', end='')
    print('')
# 答案
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
