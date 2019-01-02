from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# 我们先创建一个Series并设置层次化索引
test_index = Series(np.random.randn(10),
                    index = [['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                             [1, 2, 3, 1, 2, 3, 1, 2, 1, 2]])

print(test_index)
print(test_index.index)
print(test_index['a'])
print(test_index.ix[['b', 'd']])
print(test_index.ix[:, 1])     # 由此可见，在Series中也出现了二维索引的调用，原先的行坐标相当于最外围索引

# 将二维索引数据转换为DataFrame，类似与excel中的数据透视表
print(test_index.unstack())
print(test_index.unstack().stack())

# DataFrame可以在行列分别建立层次化索引
test_df = DataFrame(np.arange(12).reshape((4, 3)),
                    index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                    columns=[['A', 'B', 'C'], ['d', 'e', 'f']])
print(test_df)

# 而后行列的索引都可以具有名字
test_df.index.names = ['cha', 'num']
print(test_df)

# 我们尝试对这个DataFrame通过索引进行调用
print(test_df[['A']])
print(test_df.ix[['a']])
print(test_df.ix['a'])
print(test_df.ix['a','A'])

# 交换索引次序
print(test_df.swaplevel('cha', 'num'))

test_df.columns.names = ['big', 'small']
print(test_df)

print(test_df.swaplevel('big', 'small', axis=1))


# 根据级别进行汇总统计
print(test_df.sum(level = 'cha'))

# 列与行索引的相互转换
test_df_2 = DataFrame({'a' : range(7),
                       'b' : range(7, 0, -1),
                       'c' : ['a', 'b', 'c', 'd', 'e', 'f', 'g']})
print(test_df_2)

print(test_df_2.set_index(['a', 'b']))

print(test_df_2.set_index(['a'], drop=False))

test_df_3 = test_df_2.set_index(['a'])

print(test_df_3.reset_index())
