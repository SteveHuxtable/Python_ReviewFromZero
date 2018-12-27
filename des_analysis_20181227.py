from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# 我们今天学习采用pandas的描述性统计分析基础

stu_result = DataFrame({'name' : ['Steve', 'Bob', 'Jerry', 'Catherin'],
                        'math' : [90, 87, 92, 76]},
                       index=[0, 1, 2, 3])

stu_result['physics'] = [89, 99, 88, 71]

stu_result = stu_result.sort_index(by = 'math')

stu_result = stu_result.reindex(columns=['name', 'math', 'physics'])

print(stu_result)

# 我们先复习了下对DataFrame的操作
# 现在我们有了一个迷你的学生成绩单

# 输出每列的和
stu_pure_result = stu_result.ix[:, ['math', 'physics']]
stu_pure_result = DataFrame(stu_pure_result)

print(stu_pure_result.sum())
print(stu_pure_result.sum(axis = 1))

# 求最大值的索引
print(stu_pure_result.idxmax())
print(stu_pure_result.idxmin())

# 求累计值
print(stu_pure_result.cumsum())
print(stu_pure_result.cumprod())
print(stu_pure_result.cummax())
print(stu_pure_result.cummin())

# 一次性产生一系列描述性统计结果
print(stu_pure_result.describe())

# Series也有describe()方法
history = Series([97, 99, 89, 79], index=range(4))
print(history.describe())
# 需要注意，describe()方法最好处理数值型数据，如果是其他类型数据则数据意义不大

# 我们考虑如何进行相关系数和协方差计算

cov_data = DataFrame(np.random.randn(4, 3), columns=['one', 'two', 'three'],
                     index=list('abcd'))
print(cov_data)

# 下面的语句是计算1列和2列的相关系数
print(cov_data.one.corr(cov_data.two))
# 计算协方差
print(cov_data.one.cov(cov_data.two))
# 输出完整的相关系数
print(cov_data.corr())
# 输出完整的协方差矩阵
print(cov_data.cov())

# 可以用corrwith方法计算一个DataFrame中每一列和另外一个列的相关系数
print(cov_data.corrwith(cov_data.two))

# 我们最后看下如何处理缺失数据
test_na = Series([9, 8, 90, 18, np.nan, 18], index=range(6))
print(test_na.isnull())
print(test_na[test_na.isnull()])
print(test_na[test_na.notnull()])
print(test_na.dropna())
print(test_na.fillna(999))

test_df_na = DataFrame([[1, 2, 3, np.nan],
                       [np.nan, np.nan, np.nan, np.nan],
                       [9, 7, 0, 10],
                       [76, 17, np.nan, 97]])
print(test_df_na)
print(test_df_na.dropna())   # 有缺失值就删除
print(test_df_na.dropna(how='all')) # 仅删除全是缺失值的列

# 用fillna()可以填充缺失值
print(test_df_na.fillna(999))
print(test_df_na.fillna({0:9, 1:99, 2:999, 3:9999})) # 对不同的列可以填充不同的值

test_df_na.fillna({0:9, 1:99, 2:999, 3:9999}, inplace=True)
# inplace=True 则原DataFrame被就地修改
print(test_df_na)

#
