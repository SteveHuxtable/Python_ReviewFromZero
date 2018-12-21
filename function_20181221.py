from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# 我们今天学习如何在python中编写函数

# python是一个兼容函数式编程和面向对象编程的编程语言。在python中编写函数式简单的
def print_hello():
    print("Hello World!\n")
    temp = input("please input your name:")
    print("Nice to meet you! " + temp)


print_hello()
# 我们先将函数理解为将某种代码可执行的功能的打包

# 函数的很重要的意义就是先从环境中获取输入，而后进行运算，最后将结果输出。
# 我们可以向函数传入参数
def add(a = 1, b = 2):
    print(a + b)

add()
add(2, 5)
add(b = 6, a = 5)

# 由以上加法函数的编写和调用，我们发现
# 函数的参数是可以有默认值的，比如参数列表中a=1，这个1就是默认值，当实际调用时没有进行修改，那么就以默认值为准
# 参数分为实际参数（实参）和形式参数（形参）
# 形参是在定义函数时参数列表中的，就是add()中的a和b
# 实际参数则是要由函数外部传递给形参的，就是add(b = 6, a = 5)中的a和b(因为已经获得了赋值)

# 函数的参数顺序很重要，比如上面的add(2, 5)，我们没有指定a和b各是什么，于是实参就按顺序传递给形参
# 那么你明白add(b = 6, a = 5)的意义了么？

# 我们的实参于是有了三种：位置实参（看顺序往函数传值）、关键字实参（显式指定实参的传入值是什么）、默认实参

# 函数如何返回计算之后的结果？
def minus(a = 2, b = 1):
    return(a - b)

print(minus(100, 101))

# 在后续的学习中我们将学习泛函，即“函数的函数”，用泛函机制可以极大丰富函数式编程的功能
# 在今天，我们还无法理解泛函，学了也没啥意义。我们先尝试写下参数为3个数或两个数的加法函数
def add(num1 = 1, num2 = 2, num3 = 'NaN'):
    if(num3 == 'NaN'):
        return(num1 + num2)
    else:
        return(num1 + num2 + num3)

print(add(1, 3))
print(add(1, 100, 1000))
# 实际上这里进行了一次条件判断，但这种做法其实只是权宜之计，后续我们学习泛函后将明确如何构造参数数目不确定的函数

# 除了返回简单的整数、字符、字符串等，函数可以返回很复杂的数据类型（比如字典、Series、DataFrame等）

# 比方说我们想写一个DataFrame，随机存储一个班同学的语文、数学和英语的三科成绩

def input_exam_result(code = ''):
    exam_result = DataFrame(columns=['Math', 'English', 'History'])

    if(code == '19941227'):
        print("Please input the result of your students!")
        while(True):
            if_return = input("Do you want to input a new student's result?[y/n]")
            if(if_return == 'n'):
                return(exam_result)
            elif(if_return == 'y'):
                temp_id = input("Please input ID of the student : ")
                temp_math = input("Please input Math of the student :")
                temp_english = input("Please input English of the student :")
                temp_history = input("Please input History of the student :")

                # how to insert a row into a DataFrame
                exam_result.loc[temp_id] = [temp_math, temp_english, temp_history]
            else:
                print("Please input y or n")
    else:
        print("Please input the correct code of you")
        return

my_table = input_exam_result('19941227')
print(my_table)

# 看到以上这个输出之后，我们就弄明白了如何写一个还算复杂的函数，以及将一个DataFrame作为函数运行的结果返回

