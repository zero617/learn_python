"""练习1：在屏幕上显示跑马灯文字。"""
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
