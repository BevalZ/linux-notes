# <center>  《python 从入门到实践》</center>

##一、环境以及安装编辑器
###推荐编辑器：Geany
1. 安装Geany：
- sudo pacman -S geany
- sudo apt install -y geany
- sudo yum install geany
2. 配置geany  
 Build --> Set Build Commands:
 Compile: python3 -m py_compile "%f"
 Execute: python3 "%f"

 ##二、变量和简单数据类型
 ###变量名建议
 1. 变量名应既简短又具有描述性。例如,name比n好,student_name比s_n好,name_length
比length_of_persons_name好
2. 慎用小写字母l和大写字母O,因为它们可能被人错看成数字1和0
###字符串
1. print(variate.upper())  
>在这个示例中,小写的字符串存储到了变量variate中。在print() 语句中,方法
title()出现在这个变量的后面。方法是Python可对数据执行的操作。在variate.title()中, variate后面的句点(.)让Python对变量name执行方法title()指定的操作。每个方法后面都跟着一对括号,这是因为方法通常需要额外的信息来完成其工作。这种信息是在括号内提供的。函数title()不需要额外的信息,因此它后面的括号是空的。

2. print(variate.upper())
> 转变成大写
3. print(variate.lower())
> 转变成小写
4. 合并字符串
>Python使用加号(+)来合并字符串  
5. 使用str()避免类型错误
> str(variate) 可以讲括号内的变量转变为字符串  
###空白
1. 使用制表符或换行符来添加空白
要在字符串中添加制表符,可使用字符组合\t ；要在字符串中添加换行符,可使用字符组合\n:
2. 删除空白
剔除字符串开头、结尾的空白,或同时剔除字符串两端的空白。为此,可分别使用方法
lstrip()、rstrip()和strip():

##三、列表
###列表的概念
1. 在Python中,用方括号([])来表示列表,并用逗号来分隔其中的元素。
2. Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为 -1,可让Python返回最后一个列表元素:索引-2返回倒数第二个列表元素,索引-3返回倒数第三个列表元素,以此类推  

###列表修改
1. 修改元素：如下  
```
INPUT
----------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
----------------------------------------------------
OUTPUT
----------------------------------------------------
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
----------------------------------------------------
```

2. 在列表末尾添加元素  
```
INPUT
----------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
----------------------------------------------------
OUTPUT
----------------------------------------------------
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
----------------------------------------------------
```
>方法append()让动态地创建列表易如反掌,例如,你可以先创建一个空列表,再使用一系列的
append()语句添加元素

3. 在列表中插入元素  
使用方法insert()可在列表的任何位置添加新元素
```
INPUT
----------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
----------------------------------------------------
OUTPUT
----------------------------------------------------
['ducati', 'honda', 'yamaha', 'suzuki']
----------------------------------------------------
```
4. 从列表中删除元素  
>如果知道要删除的元素在列表中的位置,可使用del语句如：del motorcycles[0]； <br> 删除列表末尾的元素使用方法pop():如下
```
INPUT
----------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
----------------------------------------------------
OUTPUT
----------------------------------------------------
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
----------------------------------------------------
```
>实际上,你可以使用pop()来删除列表中任何位置的元素,只需在括号中指定要删除的元素
的索引即可
别忘了,每当你使用pop()时,被弹出的元素就不再在列表中了。
如果你不确定该使用del语句还是pop()方法,下面是一个简单的判断标准:如果你要从列表
中删除一个元素,且不再以任何方式使用它,就使用del语句;如果你要在删除元素后还能继续
使用它,就使用方法pop()  
根据值删除元素
有时候,你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值,可使
用方法remove()

>△方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次,就需要
使用循环来判断是否删除了所有这样的值

5. 组织列表
> 使用方法 sort()对列表进行永久性排序;按与字母顺序相反的顺序排列列表元素,为此,只需向 sort() 方法传递参数reverse=True。

>  使用函数 sorted()对列表进行临时排序,同理相反的顺序排列列表元素,为此,只需向 sort() 方法传递参数reverse=True。

> 要反转列表元素的排列顺序,可使用方法 reverse()

> 使用函数len()可快速获悉列表的长度

###循环
1. for循环
```
for 临时变量 in 变量:
  do
```
2. range()函数
```
INPUT
----------------------------------------------------
for value in range(1,5):
print(value)
----------------------------------------------------
OUTPUT
----------------------------------------------------
1
2
3
4
----------------------------------------------------
```
3. 要创建数字列表
>可使用函数list()将range()的结果直接转换为列表

```
INPUT
----------------------------------------------------
numbers = list(range(1,6))
print(numbers)
----------------------------------------------------
OUTPUT
----------------------------------------------------
[1,2,3,4,5]
----------------------------------------------------
```
> rarge(* , &ensp;&ensp;* ,&ensp;&ensp; * )<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|<br>
&ensp;&ensp;&ensp;&ensp;&ensp;开始 结束 步距

4. 数字列表简单统计计算
> 函数：min(),max(),sum()

5. 列表解析
>列表解析将 for循环和创建新元素的代码合并成一行,并自动附加新元素
```
INPUT
----------------------------------------------------
squares = [value**2 for value in range(1,11)]
print(squares)
----------------------------------------------------
OUTPUT
----------------------------------------------------
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
----------------------------------------------------
```
6. 列表切片
>如 print(players[1:4])
输出第2-4的元素
print(players[:4])
从首位开始输出到第四位
print(players[2:])
从第三位开始输出到末尾
print(players[-3:])
倒数三个元素

7. 遍历切片
> 使用for循环

8. 复制列表
> a=b[:] 此时a复制了b中的元素，a，b改动相互独立 ；若a=b，则a随b改动

9. 元组
> 与列表相近，但是不可更改，格式为a(1,2,3)；更改方式为重新定义a=(,)

##四 if语句
###基本格式
1. if语句基本格式
```
if condition :
    do
else:
    do
```
2. if-elif-else句式
```
if condition:
  do something
elif condition:
  do something
else:
  do something
```
3. else
> else 是当if 和 elif 条件均不满足的所有情况都执行，所以不建议使用，最好使用一条elif进行清晰说明

### 条件测试
1. “与”、“或”
  and
  or  
2. 检查特定值是否包含在列表中  
'char' in a
'char' not in a

3. 布尔表达式
```
variate=Ture
variate=False
```

###用if语句处理列表
1. 检查特殊元素
> for 循环中加入if语句

2. 确定列表不是空的
> 。在if语句中将列表名用在条件表达式中时,Python将在列表
至少包含一个元素时返回True,并在列表为空时返回False。

3. 多个列表
> for a in 列表 1：
    if a in 列表2：
      do something
    if a not in 列表2：
      do something
## 六、字典  
### 字典的概念
1. 基本格式
 > 在Python中,字典是一系列键—值对。每个键都与一个值相关联,你可以使用键来访问与之
相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上,可将任何Python对
象用作字典中的值。  

  如下：
```
alien_0 = {'color': 'green', 'points': 5}
```
