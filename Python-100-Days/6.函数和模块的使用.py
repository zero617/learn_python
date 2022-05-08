"""
实现计算求最大公约数和最小公倍数的函数。
"""


def gys(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def gbs(x, y):
    """求最小公倍数"""
    return x * y // gys(x, y)


if __name__ == '__main__':
    a = int(input("请输入a："))
    b = int(input("请输入b："))
    print("最大公约数是%d, 最小公倍数是%d" % (gys(a, b), gbs(a, b)))

"""
实现判断一个数是不是回文数的函数
"""


def is_palindrome(a):
    a = int(input("请输入a:"))
    total = 0
    temp = a
    while temp > 0:
        total = total * 10 + a % 10
        temp //= 10
    return total == a


"""
实现判断一个数是不是素数的函数
"""


def is_prime(i):
    for a in range(2, int(i ** 0.5) + 1):
        if i % a == 0:
            return False
    return True if i != 1 else False


"""
写一个程序判断输入的正整数是不是回文素数
"""

if __name__ == '__main__':
    num = int(input("请输入数字："))
    if is_palindrome(num) and is_prime(num):
        print("%d是回文素数" % num)
