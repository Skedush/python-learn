for letter in 'Runoob':     # 第一个实例
   if letter == 'R':
      break
   print ('当前字母为 :', letter)

var = 10                    # 第二个实例
while var > 0:              
   print ('当前变量值为 :', var)
   var = var -1
   if var == 5:
      break
 
print ("Good bye!")


for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
print ("Good bye!")


 
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')


for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")


'''
pass作用 占位符
'''
def add(a,b):
    pass

for n in range(2, 10):
    pass

sum=add(1,2)

'''

'''


def max(a, b):
    if a > b:
        return a
    else:
        return b

a = 4
b = 5
c=a
if(a<b):
    c=b

print(max(a, b))


# 定义函数
def printme( str ):
   # 打印任何传入的字符串
   print (str+'123')
   return
 

 
# 调用函数
printme("我要调用用户自定义函数!")
printme("我要调用用户自定义函数!")
printme("我要调用用户自定义函数!")
printme("我要调用用户自定义函数!")
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")


print("我要调用qwe函数!123")
print("我要3wr义函数!123")
print("我要调用234义函数!123")
print("我要调wer定义函数!")
print("我要调用wer函数!")
print("再次调用同一函数")


a=1
b=10
(1,2,3,4)
def max(a, b):
    a[1]=3
max(a, b)
print(a)


def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(id(a))
change(a)


def changeme( mylist ):
   "修改传入的列表"
   mylist=[1,2,3]
   print(id(mylist))   # 一个新对象
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)
print(id(mylist))   # 一个新对象



'''
关键字参数
'''

#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )


'''
默认参数
'''

 
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )


'''
不定长参数
'''

# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
   print(vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )



# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
   print(vardict.get('a'))
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)


def f(a,b,*,c):
    return a+b+c

f(1,2,c=3)


x = lambda a,b,*args, **kwargs : a+b + 10
print(x(5,1,2,3,a=1,b=2))
print(x(0,1))


def myfunc(n):
    def add(a):
        return a * n
    return add

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


def add(a):
    a+1
    return None

a1=add(a)
print(a1)
 

print(bool(-1),bool(100),bool(0),bool(''),bool('123'),bool(None))
if None:
    print(111)


a='1+2+3+4+5-3/5\*1'
print()