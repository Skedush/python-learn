
'''
1. 编码
'''
# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
2. 注释
'''

# 请问
# 王企鹅

'''
第三注释
第四注释
'''
"""
qwewe 
"""
# 设置name为张三
name='张三'   


'''
3.行与缩进
'''

if True:
    print ("True")
else:
    print ("False")


if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    print ("False")    # 缩进不一致，会导致运行错误


'''
4. 多行语句
'''

total = '张三' + \
        '李四' + \
        '王五'

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']



'''
5. Number数据类型
'''
a=1
b=1.1
f=False
t=True

print(0==False)
print(1==True)

com=1+2j
print(com)

'''
6. 字符串
'''

name='张三'
name1='''
    张三
    李四
    '''
name1

m='张三\n李四' + "测试"
print(m)


str='123456789'

print(str[0:9])            # 输出从第三个开始到第五个的字符
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:6:3])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 3)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


'''
6. input输入
'''

inp=input("\n\n按下 enter 键后退出。")
print(inp)
print(inp)


'''
7. 同一行显示多条语句
'''

print(' 111\n');print('222')


'''
8. 多个语句构成代码组
断言
'''

if 1==0 : 
   print('1==0') 
elif 0==0 : 
   print('0==0') 
else : 
    print('else')


'''
9. print 输出
'''

x="a"
y="b"
# 换行输出
print( x ,end='\n')
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()



'''
10. import语句
'''

from day02_2 import *
print(imp1)
print(imp2)