# 昨天我们在代码的最后已经写过了一个循环，先复习下。

name_list = ["steve", "justin", "ben", "bob"]
name_list.sort()
print(name_list)

for name in name_list:
    print(name)

# 我们先进行了排序，而后遍历了整个列表, 我们能不能遍历列表的一部分呢？
for name in name_list[0 : 2]:
    print(name)

'''
我们这里就终于遇到了python语法中也说不上好，也说不上不好的一个特性，那就是“缩进”。
python利用缩进构成了“代码块”， 比如上面的for循环就是一个代码块，只有正确缩进，编译器才能知道怎么正确解释代码。
代码的功能也就才是正常的。不要着急，只要慢慢学习python，总会犯缩进错误！

还有就是for循环语句后面务必要写“：”,在：的下一行再写循环体。
'''

# 使用range()函数生成数字列表

print(range(0, 10))

for num in range(0, 10):
    print(num)

# 一定要记住range()返回的是个左闭右开的整数列

# list函数可以将range返回的整数列直接转换为整数列表

print(list(range(0, 10)))

print(list(range(0, 20, 2)))

# 我们尝试创建一个平方数的列表

square_num = []
for num in range(0, 11):
    square = num**2
    square_num.append(square)

print(square_num)

# 这里我们复习了append(self)函数、for循环写法， 以及2次方的写法（**2）

square_num = []

for num in range(0, 11):
    square_num.append(num**2)

# 在我们有了一个数字列表后，我们可以对这串数字进行简单的统计描述

print("min:")
print(min(square_num))

print("max:")
print(max(square_num))

print("sum:")
print(sum(square_num))

# python的列表的一大强大功能就是——列表解析，它可以让你直接通过简单的语句生成列表

square_num = [] # 先清空下square_num
square_num = [num**2 for num in range(1, 11)]
print(square_num)

# 基本的形式是：= [解析的表达式 for var in list]

# 列表可以进行切片操作，其实上文中已经有所演示

print(square_num[0:5])
print(square_num[1:6])

print(square_num[:5]) # 仅指定结尾，则从第一个开始
print(square_num[5:]) # 仅指定开头，则会一直切到结尾
print(square_num[-3:]) # 也可以使用负索引

# 切片同样可以进行遍历，上文中我们已经演示过一次了。

# 可以用列表或者切片进行复制操作
square_num_2 = square_num[:]
print(square_num_2)

'''
列表中每个元素都是可以修改的。然而，有时候我们不希望列表的元素可以被修改。
于是我们引入一种不可修改的列表，也就是——元组（tuple）
'''

# 我们首先创建一个元组，用“()”

test_tuple = (1, 2, 3, 4)

print(test_tuple[0])
print(test_tuple[1])

# 元组是不可修改的，如果尝试修改，就会报错
# test_tuple[0] = 10

# 虽然元组中元素不可修改，但是可以替换掉整个的元组

test_tuple = (2, 3, 4, 5)
print(test_tuple[0])
