# 我们已经学过了列表和元组两种数据结构，还有一种比较重要的数据结构叫做“字典”，它的应用非常多。

# 字典是由“key-value”对（键值对）构成的，比如我们构造一个学生学号和姓名的字典。

stu_key_name = {
    1 : "Steve",
    2 : "Bob",
    3 : "Joel",
    4 : "Justin"
}

print(stu_key_name[1])

# 可见，使用了字典后，我们可以用key去查询value。

# 字典的键值对是可以添加的，比如这个班又转来一个同学“Amy”
print(stu_key_name)
stu_key_name[5] = "Amy"
print(stu_key_name)

# 字典中的值是可以修改的，但是键是没法改的，毕竟这个索引是从键到值单向的。

stu_key_name[5] = "Alice"
print(stu_key_name)

# 字典中的键值对可以删除
del stu_key_name[5]
print(stu_key_name)

# 那么，字典怎么进行遍历呢？
for k,v in stu_key_name.items():
    print("Number " + str(k) + " is " + v)

for key in stu_key_name.keys():
    print(stu_key_name[key])

for key in sorted(stu_key_name.keys()):
    print(stu_key_name[key])

# 当然，字典的值也可以遍历，但是我不觉得这个有什么意义。
for value in stu_key_name.values():
    print(value)

# 相比简单地遍历字典的值，我们可能需要了解这个字典的值都有哪些，这样我们就需要去除值中的重复项，用集合就可以实现。
for unique_value in set(stu_key_name.values()):
    print(unique_value)

'''
到此为止，简单的字典内容就搞定了，
后续我们会学习下如何构造嵌套的字典和列表，从而实现更复杂的数据框等的数据结构。
在本节，我们简单学下while循环语句。
'''

# 程序大多是有交互性的，就是用户的指令需要向程序中输入，python提供了input()函数用于用户输入数据

Student_name = input("Please input your name: ")
print("Hello! " + Student_name + ", I am your father!!!")

# while循环为我们提供了持续的判断，即只有输入了正确的内容，程序才会进一步进入循环运行
Student_name = "Rock"
while(Student_name != "Justin"):
    if Student_name == "Justin":
        print("Nothing to do")
    else:
        Student_name = input("Please input Justin : ")


