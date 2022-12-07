class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。体重 %d" %(self.name,self.age,self.__weight))


class People:
    def __init__(self,name):
        self.__name = name
        
    def tell_info(self):
        pwd = input('请输入暗号>>').strip()
        if pwd == '0':
            print(self.__name)
        else:
            print('暗号错误')
            
    def set_name(self,new_name):
        if type(new_name) is str:
            self.__name = new_name
            print(self.__name)
        else:
            print('请输入字符串')

p = People('python')
p.tell_info()



# 商家类
class Merchants():
    
    platform = 'python外卖平台'
    
    def __init__(self, name, addr, tel):
        self.name = name  # 商家名字
        self.addr = addr  # 商家地址
        self.tel = tel  # 商家联系电话
        
    def reveive_order(self):
        print(f'{self.name}已经接单')
        
# 外卖小哥类
class Rider():
    
    platform = 'python外卖平台'
    
    def __init__(self, name, addr, tel):
        self.name = name  # 外卖小哥姓名
        self.addr = addr  # 外卖小哥配送地址
        self.tel = tel  # 外卖小哥电话
        
    def distribution(self):
        print(f'{self.name}正在配送')
        
# 顾客类
class Customer():
    
    platform = 'python外卖平台'
    
    def __init__(self, name, addr, tel):
        self.name = name  # 顾客姓名
        self.addr = addr  # 收货地址
        self.tel = tel  # 顾客电话
        
    def accept_delivery(self):
        print(f'{self.name}已经收到外卖')


class Personnel_information():
    platform = 'python外卖平台'
    
    def __init__(self, name, addr, tel):
        self.name = name  
        self.addr = addr 
        self.tel = tel 
    
    def call(self,tel):
        print(self.tel+'---->'+tel)
        
# 商家类
class Merchants(Personnel_information):
        
    def reveive_order(self):
        print(f'{self.name}已经接单')
        
# 外卖小哥类
class Rider(Personnel_information):
    
    def distribution(self):
        print(f'{self.name}正在配送')
    
# 顾客类
class Customer(Personnel_information):
    
    def accept_delivery(self):
        print(f'{self.name}已经收到外卖')

m=Merchants('十足','上海路88号','15888888888')
m.reveive_order()
m.call('15777777777')


class Test():
    
    def t1(self):
        print('from Test t1')
        
class Foo(Test):
    
    def t1(self):
        print('Foo f1')
        
f = Foo()
f.t1()
# 运行结果


class Test():
    
    def __t1(self):
        print('from Test t1')
    
    def t2(self):
        self.__t1() 
        print('from Test t2')
        
class Foo(Test):
    
    def __t1(self):
        print('Foo t1')
        
f = Foo()
f.t2()
# 运行结果


class Animal:
    
    def talk(self):
        print('动物会发出的声音...')
        
class Cat(Animal):
    
    def talk(self):
        super().talk()
        print('喵喵')
        
class Dog(Animal):
    
    def talk(self):
        super().talk()
        print('汪汪')
            
# 产生对象
cat = Cat()
dog = Dog()
# 调用方法
cat.talk()
dog.talk()


class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1)
print (v1 + v2)


a=1
a='123'
a=dict()




