# 本节我们开始面向对象编程的实例学习

# 我们写个小狗类，其中包含了小狗的基本属性（名字、年龄）和小狗的两个功能（坐和打滚）

class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

# 我们现在编写了一个dog类
    # 我们进行几点说明
    """
    1. 类的名称要首字母大写
    2. Dog()内没有其他的类，说明这个狗类没有父类
    3. 类中的函数称为方法，__init__()是一个特殊的方法，即初始化方法，用于对类的属性进行初始化
    4. 以self.为前缀的属性可供类中所有的方法使用  
    """

# 我们现在创建类的实例
my_dog = Dog('Steve', 6)

# 此时我们获得了Dog类的实例——my_dog，之后my_dog中的方法就可以被调用了
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 类的实例通常用小写的下划线式命名
# 访问属性的方法是：实例名.属性比如
print(my_dog.name)
# 调用类的方法：实例名.方法
my_dog.sit()
my_dog.roll_over()

# 类可以用来模拟世界中的真实场景，创建了实例后，我们可以通过多种方法修改实例的属性
# 比如我们可以直接通过赋值的方式进行修改
my_dog.name = "Huxtable"
my_dog.sit()
# 我们看到属性已经被修改了

# 此外，我们可以通过方法对属性进行修改，我们重写Dog类
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

    def rename(self, new_name):
        self.name = new_name

my_new_dog = Dog("Steve", 10)
my_new_dog.rename("Jeff")
my_new_dog.sit()

# 我们看到，通过rename()方法，我们修改了my_new_dog中的self.name属性

# 下面我们介绍下继承的概念
# 我们上文中提到Dog类编写时，Dog()括号中的内容是空的，说明没有继承任何父类
# 然而，很多时候我们需要继承机制，比如有一类狗会唱歌，那么我们这种唱歌狗就可以从简单狗来继承o

class SingDog(Dog):

    # 这个子类的初始化方法需要从父类继承
    def __init__(self, name, age):
        super().__init__(name, age)

    def sing_a_song(self, song):
        print(self.name.title() + " can sing " + song)

my_sing_dog = SingDog("Steve", 12)
my_sing_dog.sing_a_song("dingling dingling")

# 我们这里涉及了继承和方法重写的概念。
# 所谓继承，就是将父类的全部属性和方法继承过来
# 而方法重写指的是在子类定义过程中可以修改父类中的方法

# 下面我们介绍一种很有意义的构造类的方法——类的嵌套
# 学习完这个知识后，我们也就明白了之前使用pandas模块时的一些细节
# 可以将内容很多的类进行拆分，比如狗会跑步，我们可以先写一个跑步的类来存好
class Run():
    def __init__(self, speed, distance):
        self.speed = speed
        self.distance = distance

    def print_distance(self):
        print("has run " + str(self.distance))

    def print_speed(self):
        print("The speed is " + str(self.speed))

"""
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.run = Run()     # 我们将一个类赋给了一个Dog类的属性

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

    def rename(self, new_name):
        self.name = new_name

my_last_dog = Dog("Steve", 20)   # 我们这里尝试创建了一个Dog()类的实例

"""

# 结果发现，由于缺少对内层嵌套的Run的初始化，这个实例无法创建
# 由此可知，我们不能将类赋值给另一个类的属性，而是要将创建的实例进行赋值
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.run = Run(50, 100)     # 我们将一个类赋给了一个Dog类的属性

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

    def rename(self, new_name):
        self.name = new_name

my_last_dog = Dog("Steve", 20)   # 我们这里尝试创建了一个Dog()类的实例

# 现在发现实例创建成功了
# 而后我们尝试调用实例中的实例的属性和方法
print(my_last_dog.run.distance)
print(my_last_dog.run.print_distance())

# 我们尝试能否修改实例中嵌套的实例的属性
my_last_dog.run.__init__(1000, 1000)

print(my_last_dog.run.distance)
print(my_last_dog.run.print_distance())
# 可见，类中嵌套的实例依然保存有类的初始化方法，可以进行初始化赋值

# 此时，我们了解了面向对象编程的一些基本内容
# 同时，我们也得以理解之前使用pandas模块时的一些写法的背后内容
'''
比如 from pandas import Series, DataFrame
就是从一个叫做“pandas.py”的模块中导入两个类Series和DataFrame
而后可以调用这两个类创建实例和调用实例的方法

比如 import pandas as pd
就是将整个pandas模块全部导入，而后用“pd.类”的方法，调用这个模块中的类。
'''


