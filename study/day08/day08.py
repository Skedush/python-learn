'''
列表
'''

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x[0][x[1][1]])


# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))
print("operator.eq(c,b): ", b==c)
print("operator.eq(c,b): ", b is c)

list1 = ['Google', 'Runoob', 'Taobao']
list2=list(range(5)) # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print ("扩展后的列表：", list1)

list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print ('列表插入元素后为 : ', list1)


list1 = ['Google', 'Runoob', 'Taobao']
list1.pop()

print ("列表现在为 : ", list1)
list1.pop(1)
print ("列表现在为 : ", list1)

list4 = ['Google','Google' ,'Runoob', 'Taobao']
# del list4[0]
list4.remove('Google')
print(list4)


aList = ['Google','google','Runoob', 'Taobao', 'Facebook']
 
aList.sort()
print ( "List : ", aList)

aList = [1,22,3,45]
aList.sort()
print ( "List : ", aList)

aList = ['111111','1','03','45']
aList.sort()
print ( "List : ", aList)


def takeSecond(elem):
    return elem[1]
 
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
 
# 指定第二个元素排序
random.sort(key=takeSecond)
 
# 输出类别
print ('排序列表：', random)

list=[2,5,3,4,5,3,5]


list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list2 列表: ", list2)
print(list1 is list2)


'''
元组
'''

t=tuple('qweqwe')
print(t)


'''
字典
'''

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print(tinydict)
str(tinydict)


seq = ('name', 'age', 'sex')
 
tinydict = dict.fromkeys(seq)
print ("新的字典为 : %s" %  str(tinydict))
 
tinydict = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" %  str(tinydict))


tinydict = {'Name': 'Runoob', 'Age': 27}

print ("Age : ", tinydict.get('Age'))

# 没有设置 Sex，也没有设置默认的值，输出 None
print ("Sex : ", tinydict.get('Sex'))  

# 没有设置 Salary，输出默认的值  0.0
print ('Salary: ', tinydict.get('Salary', 0.0))


tinydict = {'RUNOOB' : {'url' : 'www.runoob.com'}}

res = tinydict.get('RUNOOB', {}).get('url')
# 输出结果
print("RUNOOB url 为 : ", str(res))



tinydict = {'Name': 'Runoob', 'Age': 7}
 
print ("Value : %s" %  tinydict.items())

for x in tinydict.items():
   print(x)

print(list(tinydict.items())[0])


tinydict = {'Name': 'Runoob', 'Age': 7}
 
print ("Age 键的值为 : %s" %  tinydict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  tinydict.setdefault('Sex', None))
print ("新字典为：", tinydict)


tinydict = {'Name': 'Runoob', 'Age': 7}
tinydict2 = {'Sex': 'female' }
 
tinydict.update(tinydict2)
print ("更新字典 tinydict : ", tinydict)


'''
集合
'''

thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
print(thisset)
x = thisset.pop()

print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
 
x.difference_update(y) 
 
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
 
z = x-y
 
print(z)
print(x)