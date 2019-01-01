# 在进行编程时，语法或逻辑的错误会导致异常（error）的产生，这个异常是我们修改程序的重要线索

# 程序返回的error也是一个对象，如果未对error进行处理，程序会返回traceback，其中包含异常的报告
# 异常可以通过try-error的机制进行处理

# print(5/0)  这是一个典型的会抛出异常的语句，这会返回一个ZeroDivisionError的异常对象
try:
    print(5/0)
except ZeroDivisionError:
    print('You cannot divide by zero!')

# 另外一个很好的处理方法是try-except-else
# 其中else的部分则是在程序未抛出error时执行
try:
    a = input("input a: ")
    b = input("input b: ")
    c = int(a)/int(b)
except ZeroDivisionError:
    print("b cannot be zero")
else:
    print(c)

# 另一个常见的额error是FileNotFoundError异常，即读取文件异常时抛出的error
try:
    with open('NotFile.txt') as file_object:
        temp_content = file_object.read()
except FileNotFoundError:
    print("There is not such a file!")
else:
    print(temp_content)

# 此外，我们可以用try-except的方式在程序抛出error时不进行处理
try:
    a = input("input a: ")
    b = input("input b: ")
    c = int(a)/int(b)
except ZeroDivisionError:
    pass                   # 采用pass语句可以直接跳过except的处理
else:
    print(c)

# 如果希望在程序的某一部分不进行任何处理的话，就可以用pass进行占位

# 代码测试是编写从小到大各个规模程序的重要步骤，如果一个程序获取多种多样的输入后都
# 能有符合程序逻辑的输出，那么这个程序就是可以接受的
# python中的unittest模块可以提供代码测试功能
import unittest

# get_formatted_name()是被测试的方法
def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

# 而后我们写一个测试的类:本例中进行的是典型单元测试
# 继承了unittest.TestCase的对象，在unittest.main()运行后，test_开头的函数都会自动执行
# 可通过的测试
class NamesTestCase(unittest.TestCase):
    def test_first_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

# 稍作修改，不能通过的测试，可以分别运行看看结果
class NamesTestCase(unittest.TestCase):
    def test_first_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis  Joplin')

unittest.main()  # 程序中所有测试类都会自动运行

# 最后解释一下，如果测试类中有setUp()方法，那么这个方法将先运行，而后再运行test_开头的方法

# 事实上，相对于前面比较顺溜的内容，这里测试的部分仅通过学习基础知识，并不好理解。
# 如果有点儿懵，也不要紧。
