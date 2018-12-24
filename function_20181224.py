# 上周的时候我们学习python中函数的编写，向python中除了传递简单的变量作为实参外，
# 可传递更复杂的列表/字典等数据类型

name_list = ['Steve', 'Kevin', 'Bob', 'Mary']

def hello(name_list):
    # 遍历传入的names_list
    for name in name_list:
        print("Hello! My friend " + name)

hello(name_list)

# 进一步，我们传入字典
math_dic = {'Steve':100,
             'Kevin':95,
             'Bob':90,
             'Mary':54}

def output_exam(exam_dic):
    for name,result in exam_dic.items():
        print("Result of " + name + " is " + str(result))

output_exam(math_dic)

'''
一个需要注意的问题是，当向一个python函数中传入列表时，对这个列表的任何修改都是永久性的，
而不是在函数作用域中先创建临时的列表副本，仅操作副本。因此进行函数中列表操作时一定需要注意。
'''

first_list = [1, 2, 3, 4, 5]
second_list = []

def first_to_second(first_list, second_list):
    while first_list:
        temp_num = first_list.pop()
        print("transfer " + str(temp_num) + " to second_list")
        second_list.append(temp_num)

first_to_second(first_list, second_list)

print(first_list)
print(second_list)

# 我们在这里其实初步看到了数据结构——“栈”应该如何实现
# 后续会专门开展python数据结构的学习，到时会重点学习

# 那么如何在python函数中传入列表的副本呢？
# 先尝试

first_list = [1, 2, 3, 4, 5]
second_list = []
first_list_temp = first_list
first_to_second(first_list_temp, second_list)
print(first_list)
print(second_list)

# 我们发现first_list还是被修改了
# 再尝试

first_list = [1, 2, 3, 4, 5]
second_list = []
first_list_temp = first_list[:]
first_to_second(first_list_temp, second_list)
print(first_list)
print(second_list)

# 成功啦！
# 进一步精简程序

first_list = [1, 2, 3, 4, 5]
second_list = []
first_to_second(first_list[:], second_list)
print(first_list)
print(second_list)

# 可见，当在函数的实参部分，将列表写为first_list[:]的形式就可以在函数中操作first_list的副本
# 而不改变first_list的实际值

# 下面的讲解内容可能有些复杂，但是对于灵活编写函数的实用性很高

# 如何传递任意数量的实参？？？

# 很多时候我们在想函数中实参时，并无法确定实参的个数，比如我们想将学生名字传入函数，之后输出
def print_names(*names):
    for name in names:
        print("-" + name)
    print("\n")


print_names('Steve')
print_names('Steve', 'Bob', 'Jacob')

# 这里看到，我们传入不等数量的实参，之后这个实参被转化为了列表，而后进行了操作

# 进一步，我们不止可以在传入不定长度的简单变量，还可以传入不定长度的“键-值对”
def print_id_names(**id_names):
    for id,name in id_names.items():
        print(id + '  ' + name)

print_id_names(a = 'Steve',
               b = 'Justin')


# 编写程序的一大要点就是程序需要清晰，其中一个很好的办法就是将函数体单独放在一个文件中
# 调用函数的部分不要和函数体放在同一个文件，构成模块，否则容易引起混乱
# 需要调用已经写好的函数时，可使用import命令（这在我们学习pandas的课程中已经见到了）
# 这也就是进行模块化编程的思想
# 我们在附注部分详细解释下如何引入别的模块的函数



