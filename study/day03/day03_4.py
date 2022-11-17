
'''
循环语句
'''


n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))



var = 1
while var == 1 :  # 表达式永远为 true
    var=var+1
    print("你输入的数字是: ", var)

#    num = int(input("输入一个数字  :"))
 
print ("Good bye!")


count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")


flag = 1
 
while (flag): print ('欢迎访问菜鸟教程!')
 
print ("Good bye!")



'''
for循环
'''

sites = ["Baidu", "Google","Runoob","Taobao"]

for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    
    if site == "Baidu":
        continue
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

for i in range(5):
    print(i)

for i in range(5,9):
    print(i)


for i in range(-10, -100, -30) :
    print(i)

for i in range(len(sites)):
     print(i, sites[i])



print(list(range(5)))