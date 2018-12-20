from pandas import Series, DataFrame
import pandas as pd
import numpy as np

print("Let's start to learn pandas!!!")

# pandas包是python中进行数据处理最常用的包，你可以把它想象成一套内容及其丰富的工具，这套工具可以
# 实现excel的几乎全部功能，而且更是集成了时间序列分析和非时间序列分析的一套方法

# 我们很容易看到：最开始的两行展示了如何使用pandas库
# from pandas import Series, DataFrame 一句，是从pandas包中载入Series和DataFrame类
# import pandas as pd 则是将整个pandas库载入运行环境，并且为其起了个pd的临时名称

# 前面的课程中我们学习了不少简单的数据结构，此时我们在pandas库中也会遇到新的数据结构，不过这些数据结构都已经是很完善但复杂的了
# Series 数据结构
obj = Series([-1, 5, 100, 105])
print(obj)

# 我们看到Series就是一个有着编号的列表
# 这其实是用类构造了一个对象，我们在今天附注部分将进行介绍和代码展示

print(obj[1])
print(obj.values)
print(obj.index)

# Series的序号我们也可以自行定义
obj2 = Series([9, 10, 11, 12], index = ['a', 'b', 'c', 'd'])
print(obj2)

# 由于创建的Series对象具有良好的索引（还可以自定义），于是其中的每个元素都可以很容易地调用
print(obj2['a'])
print(obj2[['a', 'b', 'd']])  # 这里需要注意有两重的[]
print(obj2[obj2.values > 10])

# Series对象也可以用来直接计算，当然，计算时针对值的，而不是索引
print(obj2 * 100)
# 很显然，索引不变，但是值变大了100倍

# 我们求个指数值
print(np.exp(obj2))  # 这个求指数的函数来自科学计算库NumPy，我们后续会介绍，反正先记住np.exp()的功能就是求指数

# 学到此处，是不是觉得Series对象很像个字典？对！它就是一个更优秀的字典，你也可以这么做
print('a' in obj2.index)
print('yy' in obj2.index)
print(10 in obj2.values)
# 用来判断你创建的Series对象是否有某个索引，或者某个值

# 字典对象可以直接被转换为Series对象
temp_dic = {'a':'Steve',
            'b':'Bob',
            'c':'Gavin'}
obj3 = Series(temp_dic)
print(obj3)
# 是不是很和谐！

# 我们可以传入索引，但是要注意索引的长度最好不要与原字典的长度不匹配
obj4 = Series(temp_dic, index=['a', 'b', 'c', 'd', 'e'])
print(obj4)
# 我们看到，d和e索引对应的值都是NaN，也就是python的缺失值
# 用pandas的isnull方法和notnull方法可以对Series对象中值是否缺失进行判断
print(pd.isnull(obj4))
print(pd.notnull(obj4))

print(sum(pd.isnull(obj4))) # 我们统计出了有多少个值是缺失的

# Series对象实例也有isnull()方法
print(obj4.isnull())

# 最后，Series对象自身和索引都可以起名字，这个名字后续会有用
obj4.name = 'name1'
obj4.index.name = 'name2'

print(obj4)

# 到此为止我们就学完了Series类，后面做作业熟悉下这个东西





