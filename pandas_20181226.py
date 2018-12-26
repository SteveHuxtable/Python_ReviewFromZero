from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# 我们继续学习pandas，今天完成采用pandas模块进行描述性数据分析之前的全部内容
# pandas模块的一个重要功能就是可以依据索引进行算术运算
stu_result_1 = Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
stu_result_2 = Series([2, 3, 4, 5], index = ['b', 'c', 'd', 'e'])

stu_result_all = stu_result_1 + stu_result_2
print(stu_result_all)

# 我们发现进行算术运算时，如果没有完全对齐的项就会填充为NaN。

# 进一步DataFrame也可以进行类似的操作，会从二维进行
test1 = DataFrame(np.arange(9.).reshape(3,3),
                  columns=list('bcd'),
                  index=['a', 'b', 'c'])

test2 = DataFrame(np.arange(12.).reshape(4, 3),
                  columns=list('bce'),
                  index=['a', 'c', 'f', 'e'])

print(test1)
print(test2)
print(test1+test2)

# 总结Series和DataFrame根据索引的相加，就是数据有重叠的地方就进行计算，没有重叠的地方
# 就被填充上NaN
# 如果你想不用NaN进行填充，那么可以如下

test3 = test1.add(test2, fill_value = 0)
print(test3)
# 这样test1中的所有位置都被填充上了0
# 总之，包括昨天学习的reindex函数，只要会生成NaN的地方，都可以用fill_value进行填充

# DataFrame中的行和列都可以被提取出来成为Series
df1 = test1
Ser1 = test1.ix[0]
Ser2 = test1.ix[:,0]
print(test1)
print(Ser1)
print(Ser2)

# 而后可以采用广播（broadcast）机制进行DataFrame和Series间的运算
print(test1 - Ser1)
# 学过线性代数的我们知道，利用这种机制可以很方便地进行高斯消元
# 需要注意，这种广播都是一行一行依次进行的，如果你要在列上进行，可以采用
print(test1.sub(Ser1, axis = 0))

# 由于我们跳过了numpy的学习，numpy模块的很多方法我们还不了解，不过我们可以想象那些方法都是作用于
# 各种各样的数组上的。

# np.abs()方法是求绝对值，比如
print(np.abs([-1, -2, -3])[0])

# np.abs()方法可以作用于整个DataFrame的实例上
df_3 = DataFrame(np.random.randn(4, 3), columns=list('abc'),
                 index=list('defg'))
print(df_3)

print(np.abs(df_3))

'''
警报！ 下面介绍的内容将会是非常pythonic的，那就是python的匿名函数机制
同时，匿名函数又是搭配DataFrame的apply方法的最佳伴侣.

在后期的python编程实践中，你会发现大量的匿名函数
如果某个函数只需要执行一次，那根本没有必要为其命名，毕竟命名是一个极端麻烦的事情
'''

f = lambda x: x.max() - x.min()

print(test1.apply(f))
print(test1.apply(f, axis=1))

# 今天的附注补充材料部分会讲解匿名函数的内容
# 此外，传递给apply的函数可以返回Series
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])

print(test1.apply(f))
# 这样就很容易地汇总了一个列的最大值和最小值

format = lambda x: '%.2f' % x
temp_list = [1.131, 1.3123, 1.797, 1.857]
print(df_3.applymap(format))

temp_list = Series(temp_list, index=range(4))
# applymap()方法只有DataFrame具有,因此下面的额语句时错误的
'''
print(temp_list.applymap(format))
'''
print(temp_list.map(format))

# 可以用index对数据集进行排序，比如
unsort_Ser = Series(['ju', 'duo', 'yi', 'yuan'], index=list('acbd'))
print(unsort_Ser)

sort_Ser = unsort_Ser.sort_index()
print(sort_Ser)
print(sort_Ser.sort_index(ascending=False))

# 当然也可以按值进行排序
print(unsort_Ser.sort_values())
print(unsort_Ser.sort_values(ascending=False))

# 对于DataFrame数据结构，可以指定某个列或者某些列为index，继而对整个DataFrame进行排序
# 我们再回忆下DataFrame的复杂字典构造方法
temp_df = DataFrame({'Stu_name' : ['Justin', 'Hux', 'Jacob', 'Steve'],
                     'Math_result' : [99, 88, 100, 20]})
print(temp_df.sort_index(by = 'Math_result', ascending=False))

# 我们实验下能否使用sort_values()
print(temp_df.sort_values('Math_result', ascending=False))
# 我们发现二者的功能是相同的

# 那么能否同时按照两排的元素进行复合排序呢
print(temp_df.sort_index(by = ['Math_result', 'Stu_name'], ascending=False))
# 但是当我们采用sort_value进行复合排序时就有一些捉襟见肘

# 在介绍完排序后，我们介绍下排名，即求一个Series中元素的秩
temp_Ser = Series([23, 12, -90, 24, 32, 7, 13])
print(temp_Ser.rank())
# 我们将值和秩排到一起
rank = temp_Ser.rank()
temp_df = DataFrame({'Value' : temp_Ser.item,
                     'Rank' : rank})
print(temp_df)

#