# 首先介绍下运算符“+=”（类似的自己能猜出来）

b = 1
b += 1
print(b)

b -= 1
print(b)

b *= 1
b /= 1
print(b)

# 这些就相当于 b = b + 1 的简写

# 在介绍下数据类型的转换，最典型的就是int()和str()
# 当你input获得一个数字时，其实这个数字是个字符型变量
a = input("please input a number : ")
# a > 1 # 这句会报错，因为a是个字符型变量，没办法和数字进行比较
a = int(a)
print(a > 1) # 采用int()进行转换后，就可以与数字进行比较

# 我们再介绍下求模运算符 ： %
a = 7 % 2
print(a)
# 求模运算的应用在很多算法中都会出现

# 昨天我们学习了while式循环，有两个语句可以和while循环很好的配合
# 第一个是break，执行break会退出循环
i = 1
while(True):
    i += 1
    if(i == 100):
        print("I will break!")
        break

# 另外一个是continue语句，会退出当前一次的循环，但是循环还会继续
i = 1
while(i < 10):
    i += 1
    if(i == 4):
        print("use continue")
        continue
        i += 100
    else:
        print(i)
# 很显然，执行continue后，循环继续，但是没有执行continue后面的那个i += 100

# while循环可以用来处理列表和字典的元素。for循环处理这类问题则有困难，因为用for循环遍历列表时，列表不允许修改
# 否则for循环就懵逼了

stu_list = ["Steve", "Bob", "Justin", "Chris"]

'''
for name in stu_list:
    print(stu_list.pop())
# 虽然以上的循环没有报错，但是由于做了出栈操作，列表变短。不能将所有人名pop出来。
'''

while(stu_list):
    print(stu_list.pop())

# 这样，只要stu_list不空，while循环的循环体就一直执行，最终将所有结果弹出。

# 用while循环可以删除列表中某个元素，即使元素多次出现
pet_list = ["cat", "dog", "frog", "cat", "horse", "banana", "banana"]
# 显然banana不是pet，我们于是要将两个banana从列表中删除，我们先试试用remove()
pet_list.remove('banana')
print(pet_list)
# 我们发现，remove方法只能删除一个元素
pet_list = ["cat", "dog", "frog", "cat", "horse", "banana", "banana"]
# 采用while循环，可以将banana元素彻底删除
while('banana' in pet_list):
    pet_list.remove('banana')
print(pet_list)
# 看，我们这回将两个banana都删掉了

# 最后为了收尾，我们写一个登陆学号和数学成绩的动态的字典，用while循环控制是否结束录入
if_input = True
math_dic = {}
while(if_input):
    temp = input("Do you want to input the information?[y/n] :")
    if(temp == 'y'):
        stu_id = input("Please input the ID of the student :")
        math_grade = input("Please input the math grade of the student :")
        math_dic[stu_id] = math_grade
    elif(temp == 'n'):
        break
    else:
        print("Please input y or n")

print(math_dic)

# 学到此处，python最基本的语句就都学得差不多了。再往后就是学习函数式编程和面向对象编程
# 在深入到编程范式之前，我们先脱离基本的语法学习，从明天起转向利用python进行简单的数据分析