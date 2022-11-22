'''
基本数据类型
'''

'''
Number
'''
# 键
# 值
# key
# value

print(isinstance({'name':'张三','age':12},dict))
people={'name':'张三','age':{'2022':12,'2023':[1,2]}}

print(isinstance(people.get('age').get('2023')[0],int))


int
float
complex

str
bool
list
tuple
dict

# print(True is 1)
# print(False is 0)

var1=1
print(var1)
# del var1
print(var1)

print(2**2**2)


'''
String
'''

str1 = 'Runoob'

print (str1)          # 输出字符串
print (str1[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str1[0])       # 输出字符串第一个字符
print (str1[2:5])     # 输出从第三个开始到第五个的字符
print (str1[2:])      # 输出从第三个开始的后的所有字符
print (str1 * 2)      # 输出字符串两次，也可以写成 print (2 * str1)
print (str1 + "TEST") # 连接字符串

print(r'Ru\noob')
print('Ru\noob')

'''
List
'''

l=[1,2,3]
l1=l[:]
print(l1)
l.append(4)
print(l1)

l=[1,2,3]
l1=l
print(l1)
l.append(4)
print(l1)


list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

list2=tinylist * 2 *2
print(list2)
print (list)            # 输出完整列表
print (list[1])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

str2='123'
# str2[1]='3'
print(str2)

def reverseWords(input):
     
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    # output=[]
    # for i in range(len(inputWords)-1,-1,-1):
    #     output.append(inputWords[i])
    # ['I','like','runoob']
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1]
    # print(inputWords)
    # 重新组合字符串
    # ['runoob','like','I']
    output = ' '.join(inputWords)
     
    return output
 
if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)


'''
Tuple（元组）
'''

tuple1 = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple1)             # 输出完整元组
print (tuple1[0])          # 输出元组的第一个元素
print (tuple1[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple1[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple1 + tinytuple) # 连接元组


tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

print(type(tup2))


'''
Set（集合）
'''


sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu','Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

if {1,2} in [1,2,{1,2}]:
    print('True')

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
a1 = set([1,2,3,4,1,2,3])
a2={1,2,3,4}
b = set('alacazam')

i=1
i=int(1)

c = set()

print(a)
print(a1)
print(a2)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素


'''
Dictionary（字典）
'''
p={'age':13}
p.update(age=12)
dic={'age':p.get('age')}

print(dic)

dict1 = {}
dict1['one'] = "1 - 菜鸟教程"
dict1[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict1['one'])       # 输出键为 'one' 的值
print (dict1[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

dict1={}
dict1[0]=0
dict1[1]=1
dict1[2]=2
dict1[3]=3
print (dict1)           # 输出键为 2 的值

d=dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])


print({x: x**2 for x in (2, 4, 6)})

dict(Runoob=1, Google=2, Taobao=3)


print(int(1.2))
print(int(1.9))
print(int('1'))

print(int('11010101',2))


print(repr('1231\n23'))
print(str('12\n3123'))
print(str({'age':13}))
print(repr({'age':13}))

print(eval( '3 * 2' ))

a=set('abcd')
print (a)

dict([('one', 1), ('two', 2), ('three', 3)])

print( chr(0x30), chr(0x31), chr(0x61))