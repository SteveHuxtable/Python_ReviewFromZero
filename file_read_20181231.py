# python提供了一次完整读取文件和逐行读取文件的两种方式

# 读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# with关键字是比较智能的文件打开和关闭的命令，避免了手动open()和close()引起的问题
# 当然，我们可以手动打开文件
f = open('pi_digits.txt', 'r')
print(f.read().rstrip())
f.close()

# 我们可以使用相对路径读取其他文件夹中的文件
with open('text_files\pi_digits_2.txt') as file_object_2:
    contents = file_object_2.read()
    print(contents)
# 可见，在windows系统中，路径分隔应该使用“\”

# 上面我们介绍了两种读取整个文件的方法
# 另外一种较好的处理文件的方法是逐行处理

with open('pi_digits.txt') as file_object_3:
    for line in file_object_3:
        print('new line:')
        print(line)
# 我们看到，整个文件中的内容被一行一行地输出了。
# 当我们要处理的文件非常大时，为了缓解内存的压力，逐行读取的方式更加合适

# 逐行读取时，我们可以消除每行末尾的换行符
with open('pi_digits.txt') as file_object_4:
    for line in file_object_4:
        print('new line: ')
        print(line.rstrip())
# 我们发现多余的行没有了

# 当我们使用with关键字时，生成的文件对象只能在with关键字的代码块内使用
# 为了能在代码块外使用，我们可以将每行提取出来，并且储存为一个列表

file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())

# 也就是说，with关键字生成的对象是仅存活在with的作用域内，
# 但是过程中生成的其他变量其实可以在with的作用于外调用，我们做个试验
with open(file_name) as file_object:
    file = file_object.read()
print(file)
# 验证成功，file也可以在with的作用域外调用

# 我们成功了创建了一个包含文件各行内容的列表lines，而后我们对其进行处理
# 如何删除一个文件每行末尾的换行符？
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

# 进一步为了删除空格，我们可使用string()而不是rstrip()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# 读取文件我们先学习到这里，之后我们学习如何写入文件
# 写文件和读文件的方法差不多
with open('test_write.txt', 'w') as file_object:
    file_object.write('I love programe')
# 我们发现我们的写文件操作已经成功了
# python向文件中只能写入字符串

# 我们可以向一个文件中依次写入多行
with open('test_pi_write.txt', 'w') as file_object:
    for line in lines:
        file_object.write(line)

# 除了文件的读写之外，python提供了一种文件操作模式叫做“附件”
with open('test_pi_write.txt', 'a') as file_object:
    file_object.write('\nadd a line in the end of the file')

# 我们最后学习下python对json格式数据的处理
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
# 采用json.dump()我们将一个列表储存进了一个json对象中f_obj
# 可见，我们的文件夹下生成了一个.json结尾的文件，打开后发现内容也是一个列表
# 而后，我们可以载入这个生成的json文件
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

# 可见我们使用json.load()将这个列表存入了numbers中


