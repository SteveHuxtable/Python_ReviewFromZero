# 我们首先复习下昨天学习的如何导入模块中的函数或类
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# 我们复习下怎么创建一个Series对象
stu_list = ['Steve', 'Huxtable', 'Hu', 'Dayu']
stu_series = Series(stu_list, index = ['a', 'b', 'c', 'd'])
print(stu_series)

# 我们创建的这个stu_series实际上是一个Series类的实例（今天会详解）
# 这个stu_series的index就是一个索引对象

print(stu_series.index)

# 索引对象的一个明显特征就是不可修改性
# stu_series.index[0] = 'e' # 这个语句会报错
# 对象不可修改，也就是说，当这个对象被创建了之后，就不可以修改了。

# index对象形式和数组（numpy的数据类型）像，它的功能也接近一个集合
print('a' in stu_series.index)

# index对象的一个重要功能就是可以对Series实例对象的元素进行重排
stu_series.reindex(['a', 'c', 'b', 'd', 'f'])
print(stu_series) # 发现stu_series没变

stu_series_1 = stu_series.reindex(['a', 'c', 'b', 'd', 'f'])
print(stu_series_1)
# 我们发现.reindex()方法并不能直接修改stu_series,而是作用在了一个副本上

# reindex()方法可以很方便地实现插值，比如向后插
stu_series = Series(data=["Hu", "Da", "Yu"], index = [0, 2, 4])
print(stu_series)
# 而后我们补全索引并插值
stu_series_modify = stu_series.reindex(range(8), method='ffill')
print(stu_series_modify)


# DataFrame类也同样具有reindex方法
# 我们超前一些，用numpy包的矩阵创建一个DataFrame
df_test = DataFrame(np.arange(9).reshape(3,3),
                    index=['a', 'b', 'c'],
                    columns=['c1', 'c2', 'c3'])
print(df_test)

df_test_2 = df_test.reindex(['a', 'b', 'c', 'd', 'e'])
print(df_test_2)

df_test_3 = df_test.reindex(columns=['c1', 'c2', 'c3', 'c4'])
print(df_test_3)

# 下面是一种很简洁的方法
df_test_4 = df_test.ix[['a', 'b', 'c', 'd'], ['c1', 'c2', 'c3', 'c4']]
print(df_test_4)

# 此时df_test_4数据框的最后一列和最后一行实际没有意义，因为全是缺失值，那么怎么删除呢？
df_test_5 = df_test_4.drop('d')
print(df_test_5)

df_test_6 = df_test_4.drop('c4', axis = 1)
print(df_test_6)

# 索引对象的存在给我们提供了丰富的方式用于对Series或DataFrame进行切片
print(df_test_4)
print(df_test_4[0:2])
print(df_test_4[0:1])
print(df_test_4['a':'c'])

print(df_test_4[df_test_4 < 5])

print(df_test_4['c1'])

# 这里只是展示了几种从DataFrame中抽取数据的方法，实际使用中请记住怎么从DataFrame中抽取
# 数据其实都很容易，到时候查一查google
# 我们将在附注中简单列举下



