"""练习1：在屏幕上显示跑马灯文字。"""
from random import randrange, randint, sample
import random
import os
import time


def main():
    content = "北京欢迎你......"
    while True:
        os.system("cls")
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()


"""练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。"""


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    code_len = int(input("请输入验证码长度："))
    print(generate_code(code_len))


"""练习3：设计一个函数返回给定文件名的后缀名。"""


def get_suffix(filename, has_dot=False):
    if 0 < filename.rfind('.') < len(filename):
        return filename[filename.rfind('.'):] if has_dot else filename[filename.rfind('.') + 1:]
    else:
        return ''


if __name__ == '__main__':
    filename = input("请输入文件名：")
    print(get_suffix(filename, True))


"""练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。"""


def max2(nums):
    nums_temp = nums.copy()
    nums_temp.sort()
    return nums_temp[-1], nums_temp[-2]


if __name__ == '__main__':
    nums = [1, 5, 9, 4, 3, 2, 6, 7, 8, 0, 1]
    print(max2(nums))
    print(nums)


"""练习5：计算指定的年月日是这一年的第几天。"""


def is_leap_year(year):
    """
    判断是否为闰年
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    """
    计算传入的日期是这一年的第几天
    """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for index in range(month - 1):
        total += days[index]
    if is_leap_year(year) and month > 2:
        total += 1
    return total + day


def main():
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入日期："))
    print(which_day(year, month, day))


if __name__ == '__main__':
    main()


"""练习6：打印杨辉三角。"""


def yh_triangle(num):
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    num = int(input("请输入行数："))
    yh_triangle(num)


"""综合案例"""

"""案例1：双色球选号。"""


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()


"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30  # 过30归0 30循环
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()
