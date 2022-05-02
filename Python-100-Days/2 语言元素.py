# 练习1：华氏温度转换为摄氏温度。
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
f = float(input('请输入华氏度：'))
c = (f-32)/1.8
print('%.1f F = %.1f C' % (f,c))

# 练习2：输入圆的半径计算计算周长和面积。
import math

r = float(input('请输入半径：'))
p = 2 * math.pi * r
s = math.pi * r * r
print('半径是%.1f 周长是%.1f 面积是%.1f' % (r, p, s))

# 练习3：输入年份判断是不是闰年。
n = float(input('请输入年份：'))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('%d是闰年' % n)
