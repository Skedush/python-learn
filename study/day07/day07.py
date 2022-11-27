'''
数据类型转换
'''


# 隐式类型转换


num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))



num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

print(num_int+num_str)


'''
显式类型转换
在显式类型转换中，用户将对象的数据类型转换为所需的数据类型。 
我们使用 int()、float()、str() 等预定义函数来执行显式类型转换。
'''

x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3

x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2

x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'


num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))


'''
Python 推导式
'''

# 列表推导式

def aaa(a):
    return a

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)


multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)


'''
Python成员运算符
'''
 
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")



'''
Python身份运算符
'''

a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")



a=1+2*3
print(a)


x = True
y = False
z = False
 
if x or y and z:
    print("yes")
else:
    print("no")



'''
Python3 数字(Number)
'''


number = 0xA0F # 十六进制
number
2575

number=0o37 # 八进制
number


width = 20
height = 5*9
width * height



tax = 12.5 / 100
price = 100.50
price * tax
price + _
round(_, 2)


print ("abs(-40) : ", abs(-40))
print ("abs(100.10) : ", abs(100.10))

import math

print ("math.ceil(-45.17) : ", math.ceil(-45.17))
print ("math.ceil(100.12) : ", math.ceil(100.12))
print ("math.ceil(100.12) : ", math.ceil(100.0))
print ("math.ceil(100.72) : ", math.ceil(100.72))
print ("math.ceil(math.pi) : ", math.ceil(math.pi))


print ("max(80, 100, 1000) : ", max(80, 100, 1000))
print ("max(-20, 100, 400) : ", max(-20, 100, 400))
print ("max(-80, -20, -10) : ", max(-80, -20, -10))
print ("max(0, 100, -400) : ", max(0, 100, -400))


print ("math.modf(100.12) : ", math.modf(100.12))
print ("math.modf(100.72) : ", math.modf(100.72))
print ("math.modf(119) : ", math.modf(119))
print ("math.modf(math.pi) : ", math.modf(math.pi))


'''
字符串
'''

var1 = 'Hello World!'
 
print ("已更新字符串 : ", var1[:6] + 'Runoob!')


print('"\
    "')


print('\\')

print('\'')

print("\a")

print("Hello \b World!")


print("Hell\rWorld!")


print ("我叫 %s 今年 %d 岁!" % ('小明', 10))


para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""

print (para_str)

name = 'Runoob'
f'Hello {name}'  # 替换变量
'Hello Runoob'
f'{1+2}'         # 使用表达式
'3'

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
f'{w["name"]}: {w["url"]}'
'Runoob: www.runoob.com'


a='str'
a.capitalize()


str="www.runoob.com"
sub='o'
print ("str.count('o') : ", str.count(sub))

sub='run'
print ("str.count('run', 0, 10) : ", str.count(sub,0,10))


str1 = "Runoobexam example....wow!!!"
str2 = "exam"
 
print (str1.find(str2))
print (str1.find(str2, 5))
print (str1.find(str2, 10))


str1 = "Runoob example....wow!!!"
str2 = "exam"

print (str1.index(str2))
print (str1.index(str2, 5))
print (str1.index(str2, 10))


s1 = "-"
s2 = ""
seq = ["r", "u", "n", "o", "o", "b"] # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
len(s1)

str = "     this is string example....wow!!!     "
print( str.lstrip() )
str = "88888888this888 is string example....wow!!!8888888"
print( str.lstrip('8') )


str = "www.w3cschool.cc"
print ("菜鸟教程旧地址：", str)
print ("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
 
str = "this is stringis isexample....wow!!!"
print (str.replace("is", "was", 3))


n = 'a0123456789'
s = "〇一二三四五六七八九"
for c in "0123456789": 
  n = n.replace(c, s[eval(c)])
print(n)


str1 = "this is really a string example....wow!!!"
str2 = "is"

print (str1.rfind(str2))

print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))

print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))



str = "this is string example....wow!!!"
print (str.split( ))       # 以空格为分隔符
print (str.split('i',4))   # 以 i 为分隔符
print (str.split('w'))     # 以 w 为分隔符