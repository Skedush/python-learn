
def add(x,y):
    return x+y

print(add)
sum=add(1,2)
print(sum)
sum1=add
print(sum1)
sum2=sum1(2,3)
print(sum2)


'''
作用域
'''

x=1
z=3
def add(x,y):
    return x+y+z

sum=add(2,2)
print(sum)

'''
函数默认值
'''

def add(x,y=1):
    return x+y

sum=add(2,10)
print(sum)


'''
函数的参数
'''

def add(x,y=1,*args):
    print(args)
    return x+y

sum=add(2,10,1,2,3,4)
print(sum)


'''
代码运行的顺序
'''

def add(x,y=1,*args):
    print(args)
    return x+y
    print(args)

print('111')
sum=add(2,10,1,2,3,4)
print(sum)

'''
函数的嵌套使用
'''
def add(x,y):
    return x+y

def sub(x,y):
    sum=add(x,y)
    return sum-y

value=sub(2,2)
print(value)

value2=add(sub(1,2),sub(2,2))
print(value2)

'''
代码死循环
'''

def add(x,y,qwe):
    qwe(x,y)
    return x+y

def sub1(x,y):
    sum=add(x,y,sub1)
    return sum-y

value3=sub1(2,2)
print(value3)




