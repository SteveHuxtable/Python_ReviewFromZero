# 我们学习下用if进行条件判断

student_id = [1, 2, 3, 4, 5]
student_names = ["Steve", "Justin", "Bob", "Gavin", "Pony"]

for id in student_id:
    if id == 1:
        print("Student name is ", student_names[0])
    else:
        print("Student name is ", student_names[1])

student = "Steve"
print(student == "steve")
print(student == "Steve")

# 由此可见，python是区分大小写的。如果你之前是搞basic编程的，那需要牢记这个。

# 除了“==”外，还有“！=”。

print(student != "steve")
print(student != "Steve")

# 比较数字则可用比较运算符
print(1 > 0)
print(1 < 0)
print(1 >= 0)
print(1 <= 0)

# python 可以使用系统保留字 and 或者 or 构成复合条件判断语句

print((1 > 0) and (2 < 0))
print((1 > 0) or (2 < 0))

# python 可以使用保留字 in ，来判断某个元素是否处在列表中

print("Steve" in student_names)
print("Jacob" in student_names)

for name in student_names:
    print(name.upper())

# 同学你还能看懂上面这个循环么？看不懂的话就复习下之前的内容
# 不要把for循环的in，和判断是否是列表元素的in弄混了

# 除了in 外，还有保留字 not in
print("Huxtable" not in student_names)
print("Steve" not in student_names)

# True 和 False 保留字是直接用于判断的变量，其实每个条件判断最终也是返回一个True或者False

if True:
    print("True")

if False:
    print("False")

# 除了“if-else”，还有更复杂的“if-elif-else”
num = 11
if num > 13:
    print("num > 13")
elif num > 12:
    print("num > 12")
elif num >= 12:
    print("num >= 12")
else:
    print("num < 12")

# 注意，上面的else并不是必须的。当所有if和elif的条件已经是排中的时，就可以不要else。

# 我们之前学习过如何对列表进行循环，问题是我们要防止对空列表进行循环，因此，进行列表循环前，我们可以对列表是否为空进行判断
empty_list = []
print(len(empty_list))
if empty_list:
    print("this is not an empty list!")
else:
    print("this is an empty list!")


