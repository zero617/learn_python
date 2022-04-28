import re
n = '13英寸'
pattern = re.compile(r"[a-w]+")
a = re.findall(pattern, n)[0]
print(a)
# if a == '英寸':
#     print('good')