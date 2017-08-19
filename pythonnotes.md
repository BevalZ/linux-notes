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
