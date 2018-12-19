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

+ 字典列表
+ 字典的值是列表
+ 字典的值是字典

2. 进一步学习while循环，并且学习continue/break等循环相关的语句

3. 使用while循环来处理列表和字典

### 附注：

