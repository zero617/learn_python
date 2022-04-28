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
