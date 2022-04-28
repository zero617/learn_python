"""
英制单位英寸和公制单位厘米互换
"""
import re

# value = input('请输入长度: ')
value = '13英寸'

pattern1 = re.compile(r"[a-w]+")
unit_list = re.findall(pattern1, value)
if unit_list:
    unit = unit_list[0]
else:
    unit = ''

pattern2 = re.compile(r"[\u4e00-\u9fa5]+")
danwei_list = re.findall(pattern2, value)
if danwei_list:
    danwei = danwei_list[0]
else:
    danwei = ''

pattern3 = re.compile(r"[0-9]+")
n = re.search(pattern3, value)
num = float(n.group())

if unit == 'in' or danwei == '英寸':
    print('%.1f英寸 = %.1f厘米' % (num, num * 2.54))
elif unit == 'cm' or danwei == '厘米':
    print('%.1f厘米 = %.1f英寸' % (num, num / 2.54))
else:
    print('请输入有效的单位')

'''
百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
'''
score = float(input('请输入成绩：'))
if score >= 90:
    print('A')
elif score <= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')

'''
输入三条边长，如果能构成三角形就计算周长和面积。
'''
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a+b > c and a+c > b and b+c > a:
    perimeter = a+b+c
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')