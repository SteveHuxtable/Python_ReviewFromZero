# string
first_string = "My name is Steve"
print(first_string)

'''
python中对象的存在非常广泛，string是一个类，创建类的实例就获得了一个对象。对象的存在最重要的意义
就是对象是可以携带“方法的”。比如：
'''

print(first_string.title())
print(first_string.lower())

# python需要数量掌握的就是1）创建对象  2）使用对象.方法()这种形式实现需要的功能

string_1 = "123"
string_2 = "456"

string_1_2 = string_1 + string_2

print(string_1_2)

# 这里回忆一下制表符和换行符的功能

print("\t" + string_1_2)
print(string_1 + "\n" + string_2)

# python中还有一些重要的格式字符，但是慢慢学习就好

# 已经提到了作为对象的字符串具有很多实用的方法，其中一种方法可以去除字符串两端空格(或左端、右端的空格)

print(" ls ".strip())
print(" ls ".lstrip())
print(" ls ".rstrip())

#############################################
# 学习数字变量

print(1 + 1 == 2)
print(1.0 + 1.0 == 2.0)
print(1.0 + 1.0 == 3.0)

# 用str()函数将数字转换为字符串变量
# print("I am " + 13 + "years old")  # this is wrong!!!
print("I am " + str(13) + "years old") # this is right!!!

#############################################
# 学习列表: 列表是python的一个复杂的数据结构

student_names = ['Steve', 'Mary', "Jack", "Bob", "Harden"]

print(student_names)
print(student_names[0])
print(student_names[1])
print(student_names[-1])

print("the most beautiful boy in the class is " + student_names[0])

# 列表创建后是动态的，其中的每个元素其实可以进行修改

student_names[1] = "Duoduo"
print(student_names)

# 此外，列表创建后当然也是一个对象，可以使用列表的方法对列表中元素进行修改
student_names.append("Justin")
print(student_names)

# 进行插入

student_names.insert(0, "Kevin")
print(student_names)

# 元素删除

del student_names[0]
print(student_names)

# or 使用.pop()方法
print(student_names.pop())
print(student_names.pop(0))

print(student_names)

# 还可以根据元素的值进行删除，比如就要删除“Harden”
student_names.remove("Harden")
print(student_names)

# 可以对列表中元素进行排序
student_names.sort()
print(student_names)

# 也可以反着排
student_names.sort(reverse = True)
print(student_names)

# sort()方法的排序是永久修改的，可以用系统函数sorted()对列表进行临时排序，如:
print(sorted(student_names))
print(student_names)
# 但实际上student_names的值没有变化

# 除了排序外，列表可以被反着打印
student_names.reverse()
print(student_names)

# 确定列表的长度
print(len(student_names))

# 我们尝试组合列表长度写一个循环：
for i in range(len(student_names)):
    print(student_names[i])

print(range(len(student_names)))  # range 返回是一个左闭右开的正整数列，此处即为0、1、2

