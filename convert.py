#! /bin/bash.env python 
# *-* coding:utf-8 *-*

import os
import sys
os.system("touch a.sh && chmod +x a.sh")
os.system("mkdir output")
print("文件会被转换在output文件夹中")
x=int(input("输入数量："))
fo = open("a.sh","r+")
for a in range(1,1+x) :
  com="mri_convert -i "+"IM"+str(a)+" -o "+"./output/IM"+str(a)+".mgz"
  fo.write(str(com))
  fo.write("\n")
  print("str(b) has been converted \n")
fo.close()
os.system("./a.sh")
os.system("rm a.sh")






