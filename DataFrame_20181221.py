import pandas as pd
from pandas import Series, DataFrame

# 我们已经学习了Series，今天我们学习pandas库中的另外一个也是最重要的数据结构——DataFrame
# 我们可以先将DataFrame视为excel中的那横竖二维的输入界面

# 构造DataFrame的一个简单方法是向DataFrame的构造器中传入一个值是列表的字典，如下
student = {
    'ID' : [1, 2, 3, 4, 5],
    'Name' : ['Steve', 'Bob', 'Gavin', 'Justin', 'Marvin'],
    'Age' : [19, 20, 18 , 20, 20]
}

student_1 = DataFrame(student)
print(student_1)

# 我们看到，这样我们构造了一个DataFrame，但是一个问题是，列按照列名的顺序进行了排列，但我们不想这样排
# 因此我们需要指示下列的顺序
student_2 = DataFrame(student, columns=['ID', 'Name', 'Age'])
print(student_2)

# 我们也可以指定每行索引的名字，默认是1,2,3这种，这个可以修改
student_3 = DataFrame(student, columns=['ID', 'Name', 'Age'],
                      index=['a', 'b', 'c', 'd', 'e'])
print(student_3)

# 如果想要查看列名，则
print(student_3.columns)

# 上节课我们学习了Series，DataFrame其实可以把每列拆成一个Series
stu_names = student_3.Name
print(stu_names)
# 或者
stu_names = student_3['Name']
print(stu_names)

# 提取出的Series中的元素可以继续索引出值
print(stu_names['a'])

# DataFrame中的元素时候可以直接获得呢？
print(student_3.Name['a'])  # 也是可以的。

# DataFrame中的元素可以进行修改
print(student_1)
student_1.Age = 20 # 一整列都被修改为20
print(student_1)

student_1.ID = range(5)
print(student_1)

student_1.Name[0] = 'Kevin'
print(student_1)
# 请注意以上的几种修改方法

# DataFrame可以进行矩阵转置
student_1 = student_1.T
print(student_1)

# 可以经列表或者Series作为新列添加进DataFrame中么？
Math = [90, 80, 82, 100, 96]
English = Series(['a', 'b', 'd', 'f', 'b'], index=[3, 1, 2, 0, 4])

'''
student_new = DataFrame(student_2, Math, English)
print(student_new)
'''

# 此时，你发现合并出现问题，原因是列表不能简单地与DataFrame合并
print(student_2)
print(English)

student_2['Math'] = Math # 这是将列表作为新列添加的正确方式
print(student_2)

student_2['English'] = English  # 这是将Series作为新列添加的正确方式
print(student_2)

# 列可以使用del函数进行删除
del student_2['English']
print(student_2)
# 这个del函数的功能似乎和之前有差异，del作用于一个对象，理应操作的是数据的副本，原student_2数据不应发生变化
# 但是从上面的例子中可以看出，student_2显然已经发生了改变
# 这里最好先记住这个奇怪的现象，后面继续深入机制的时候我们会再讨论

print(student_2.values)
# 一个DataFrame的全部value是作为列表数组的形式存在的

# 到此为止DataFrame的基本内容就学习完毕

# 后续我们将学习如何对DataFrame的索引进行操作，实现数据的筛选和描述性统计

