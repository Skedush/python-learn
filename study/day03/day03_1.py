'''
Python 中的变量不需要声明。每个变量在使用前都必须赋值，
变量赋值以后该变量才会被创建。
'''
num='1'

print(num)


'''
多个变量赋值
'''

a=b=c=1
print(a,b,c)


a1, b1, c1 = 1, 2, "runoob"
print(a1,b1,c1)

'''
Number
python2 int Long
'''

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print(isinstance(b,str))