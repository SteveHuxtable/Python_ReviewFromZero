# Python_ReviewFromZero

我们来从今天进行python编程语言的复习，希望一些顺利！

## 20181215-20181216任务

1. 安装anaconda：python的包管理软件

2. 安装pycharm（可在官网安装免费社区版本）

3. 在电脑上安装git软件（windows环境下就和安装软件一个样）

> 安装好上述的东西，我们基本配置好了python的编程环境

[Git软件安装和项目clone简明教程](http://www.runoob.com/w3cnote/git-guide.html)

[anaconda安装和与pycharm连接](https://www.jianshu.com/p/eaee1fadc1e9)

***

## 20181216学习内容更新

1. 学会在pycharm中创建工程和运行*print("Hello World!")*

2. python内容的简单学习：

    - 简单数据类型和基本运算符
    - python的最基本复杂数据类型——**列表**

> 明天我们尝试对列表进行一些更加复杂的操作，包括遍历、复制等，并且对python语言的书写规范进行说明

### 20181216附注：

今天在学习列表排序的部分，我们见到了两种排序方法：
  + sorted(列表对象)
  + 列表对象.sorted(**self**)

我们需要对两种方法进行比较。其实今天的内容中任何*对象.函数(**self**)*，都忽略了这个括号中的*self*。
这个self就是对象自身，而后我们就可以理解成，这个对象用自己具有的一个功能对自身进行了操作，比如东方不败这个对象具有拿刀子割肉的功能，最终他自宫了，而这个东方不败自己也就发生了永久改变，变不回去了。

**sorted(对象)**和**del 对象** 这些命名空间为全局的函数则不同，他们相当于临时创建了个对象的拷贝（替身），而后全部操作都作用到了这个对象的替身上，对象本身的东西没有被修改。就比如西方不败是东方不败的拷贝，那么西方不败发生改变关东方不败什么事。

很重要的是，如果我们将sorted(对象)的值返回给了原对象，那原对象才能改变，如：

``` python

东方不败.sort(self)

东方不败 = sorted(东方不败)

```

这两种方法的实现是相同的，但是第一种更加pythonic一些。

***

## 20181217增加内容

昨天已经对python的简单数据类型和复杂数据类型**列表**进行了讲解，今天我们继续学习列表的相关内容，并且会穿插一些基本的python编程入门规范的内容

1. 列表的遍历——通过列表遍历学习python的循环

2. python中for循环的写法

3. 列表解析的写法（这个比较pythonic，需要学学）

4. 元素不可修改的列表——元组(tuple)

### 附注：

良好的代码除了简洁明了外，还需要有着较好的代码格式，这个方面python格式设置指南的编写者向我们提供了python改进提案（PEP）。PEP8是被广泛使用的PEP。

可以参考：[PEP8代码格式](https://www.python.org/dev/peps/pep-0008/)
。。。python官网登陆还是挺慢......**需要强调，良好的代码规范在工业界是很重要的，但是初学者不必拘泥于此。写好代码，宝宝姐说过“唯手熟尔”。**

***

## 20181218增加内容

1. 用if进行条件判断，即相应条件判断的变形

2. 用户输入和while循环（for循环已经学了一些了）

3. 字典数据类型

### 附注：

昨天说过代码需要有良好的格式，有机会我们就说说。比如你在写一个判断语句时*if(4 > 0)*这种有空格的写法就是优于*if(4>0)*。这种不带空格的写法往往会引起我的密集恐惧症。

***


## 20181219增加内容

1. 进一步学习字典数据结构，并且学习三种复杂的复合数据结构：

+ 字典列表（列表中的元素是一系列的字典）
+ 字典的值是列表
+ 字典的值是字典

2. 进一步学习while循环，并且学习continue/break等循环相关的语句

3. 使用while循环来处理列表和字典

> 到今天为止，我们就学习了基本的python语句，疯狂地累积语法其实并不可取，所以我们从明天开始，先跳出语法的学习，开始用python进行简单的数据处理。这个过程可能持续一周，在这一周中我们会遇到没有见过的语法问题，我们捎带脚进行讲解。**excel能实现的功能，python理论上都已经实现，而且数量掌握python你会觉得数据分析的顺畅程度和优越感的获得是超过在excel用数据透视表的**

***

## 20181220增加内容：pandas基础第一课

1. [什么是pandas库?](https://blog.csdn.net/qq_33399185/article/details/60872853)

2. 如何使用pandas库中的函数？

3. pandas库中的数据结构有哪些？学习Series

### 作业：
1. 用Series类构造一个对象homework1: 索引是‘a’到‘f’这6个小写字母，对应的值是111、222、333、...、666
2. 把索引修改为‘a’到‘h’这8个小写字母
3. 之后求出homework1中的缺失值个数

### 附注——什么是类和对象？

今天我们学习了pandas库中的Series，也做了作业。实际上Series就是一个**类**，类相当于面向对象编程(OOP)中的模板，比方说女娲造人之前她总归是有一个模板的，后面的人都要按照这个模板来造，造出来的就是**对象**。对象相当于是一个成型的人，他虽然属于人，但是有着自己的名字、特长（对象具有的方法）等。

```python

一个对象 = 类(传入类中的原始参数)   # 通过类，构造了一个对象

这个对象.方法()    # 这里这个对象就可以调用自己的方法来杀人放火发挥功能了

```

以上所说的也就是面向对象编程的最浅显的内容，但是应该挺容易理解。

***

## 20181221增加内容: pandas基础第二课/函数第一课

1. pandas中另一个重要的数据结构：DataFrame

2. python中如何编写函数？

3. 写一个生成不定长度的班级同学成绩单的应用

> 在本节中我们学习了写python的函数，已经初步体会了函数的强大。
> 在本周末我们依旧会学习DataFrame和函数，掌握函数编程的一般知识

***

## 20181224增加内容：函数第二课 


> 上周末因为准备今天的组会汇报内容停更了，从今晚继续开始

1. 向python的函数中传递列表

2. 向python中传递任意数量的实参

3. 调用模块中的函数

### 附注：

1. 两种导入别的模块中函数的方法：
    > from pandas import Series, DataFrame
    > import pandas as pd
    > 第二种方法相当于将pandas模块打开，之后将所有函数复制过来，as则为这些函数创建了别名pd
    > 第一种方法仅从pandas模块中导入Series函数和DataFrame函数

## 20181225增加内容：DataFrame对索引的操作/面向对象编程第一课

1. pandas库对DataFrame索引的操作

2. 面向对象编程初步：什么是类？

    > 我们今天简单谈谈面向对象编程(OOP)。**类**是第一个重要的概念，其实人类就是一个**类**! 类包括两方面的东西
    > 就是**属性**和**方法**。属性相当于人的肌肉、骨骼、器官。方法则是人具备的功能，比如写字、看书、上厕所等    > 。面向对象编程就是先创建类，之后生成类的实例的过程。当实例产生后，这个实例就可以真正地行使功能。后续学
    > 习中我们将逐渐一遍学习编写面向对象的代码，而后逐渐深入各个概念。

> 附注1. DataFrame按索引选取数据的方法：
    +  obj[val] : 选取列
    +  obj.ix[val] : 选取行
    + obj.ix[:, val] : 选取列（更严谨的方法，第一种在一些情况下可能失败）
    + obj.ix[val1, val2] : 同时选取一些行和列
    + reindex方法 : 本节代码中已经有所展示
    + xs方法 : 根据标签选取行或列，之后返回Series
    + icol、irow方法 : 根据整数位置选取行或列，并返回Series
    + get_value、set_value方法 : 根据行索引和列索引选取单个的值

***

## 20181226更新：继续学习pandas

1. 对不同索引对象的算术运算和数据对齐

2. 对DataFrame进行函数应用和映射 

3. 数据的排序和排名

3. [python中匿名函数的用法](https://blog.csdn.net/Jerry_1126/article/details/40105135)

***

## 20181227更新：用pandas进行描述性数据分析

1. 复习对DataFrame的操作

2. 用pandas进行描述性统计分析

3. 处理数据中的缺失值

***

## 20181228更新：pandas内容的收尾

1. 层次化索引

2. 整数索引

3. 面板数据

## 20181230更新：python面向对象编程第一讲

1. python中类的概念

2. python中类和实例的创建

3. 类的继承和方法重写

4. 大类的拆分和模块中类的导入

> python是一门面向对象的高级语言，因此掌握面向对象的概念就很重要。
> 本节开始的内容介绍面向对象编程的最基本内容，在掌握这些基本概念后，我们将进入实际的项目进行事件，从而深入理解面向对象编程的概念和具体编程规范。

***

## 20181231更新：python文件的读取和写入

1. python文件的读取

2. python文件的写入

3. json格式数据的python操作（json模块）

> 到今天为止，python的基本编程语法就都学习完成了，而且我们还学习了pandas的内容。此外，我们还剩了两块比较重要的基础知识，第一个是对文件的处理，第二个是对异常的处理。我们今天开始进入python文件处理的相关内容学习。
> 后续的内容可能进度较快，遇到不明白的代码可以google下具体的含义

***

## 20190101更新：python的异常处理和代码测试

1. python的异常处理机制

2. python的代码测试模块初步

> 下面我们对unittest.TestCase类中的断言方法进行汇总

|Methods|Explain|
|------------------------|-----------------------|
|assertEqual(a, b)|a==b|
|assertNotEqual(a, b)|a!=b|
|assertTrue(x)|x == True|
|assertFalse(x)|x == False|
|assertIn(item, list)|item in list|
|assertNotIn(item, list)|item not in list|

***

## 20190102更新：pandas模块继续学习

1. Series和DataFrame的层次化索引：低维度处理高维度数据，**类似于数据透视表的操作**

2. 层次化索引重排分层次序，进行不同级别的汇总统计

3. DataFrame的列和行索引的相互转换

***

## 20190103更新：numpy模块学习

numpy中的多维数组对象——ndarray（我将其记为n-dimentional array）

+ 如何创建ndarray

+ ndarray的数据类型

+ ndarray数组的广播机制（broadcasting）初步实例

+ 多维ndarray的切片和索引

> 今天的任务有点儿多，晚上就先更新到这里，明天从更复杂布尔型索引进行介绍

## 20190105更新：采用matplotlib进行python数据可视化

1. 安装matplotlib

2. 绘制简单折线图：plot(x,  y, linewidth = 5)

3. 绘制简单散点图 ：plt.scatter(x, y)

4. [散点图的颜色映射](https://matplotlib.org/tutorials/colors/colors.html)：颜色可额外为数据图增加一个维度的信息

## 20190106更新：实例学习——采用matplotlib生成随机漫步的图像

1. [什么是随机漫步？](https://www.bilibili.com/video/av19283960/) ：这个介绍视频有意思

2. 用随机函数choice()从列表中抽取随机数

3. 用matplotlib模块绘制随机漫步图

4. [学习用pypal创建图表](http://www.pygal.org/) 
    + [如何在anaconda中安装pygal模块](https://anaconda.org/akode/pygal)






