#!/usr/bin/env python
# -*- coding: utf-8 -*-


#为了跨平台，解释器
#-*- coding !!!!!!!!!!!!!!!!!!!!!!
#把txt文件中的内容从磁盘读取到内存中，然后CPU执行运算，把内存中的数据输出到cmd中
#Ram 动态内存，速度很快，断电数据丢失，存储时间在ms级，即它存储的数据1~2ms就丢失。
#我们运行的时候没感觉到它的易失性，是因为CPU一直在往里面重写。
#CPU的运行速度是ns级;磁盘的速度是s级，断电数据不丢失
#打开文件的两种方式：open，file，with

f=open('data.txt')
#f=open('data.txt','rb') #r:reading b:二进制文件。以二进制方式读取txt文件
print f.read()
f.close()



f=open('data.txt','wb')
list1 = f.read() #read是一次性把txt中的内容读取到内存中
list2 = f.readlines()#readlines()是一行一行的转换成一个list
	for line in f.readlines():
		print line.strip() #把list中的元素规整地打印出来
f.seek(0)#前面已经read一次，read是把文件中的内容都读出来，指针指向了文件的最后。后面还要让List3中存入txt内容，需要把指针挪回头上
list3 = f.read()
f.close()


f=open('data.txt','wb')
for line in f:
	print line,
f.close()



with open('data.txt','rb') as f:
	print"===="
	print f.read()
#用with opent打开一个对象，把内容赋值给f。当循环结束，f自动关闭，无需手动关闭文件。


#写文件
DATA="""
This is a poem.
life is short.
"""
#三个"""后面有换行，三个"""前也有换行，这两个换行都被写到txt里面了
fp=open('aaa.txt','wb')#如果用写的模式来打开一个已经存在的文件，会清空它
fp.write(DATA)
fp.close()


f1=file('data.txt','rb')
print f1.read()




#若要读取的文件较大，比如大于内存8G，需要用到迭代器
f=open('data.txt','rb')
for line in f:
	print line,
f.close()


#切片
string ='bacon ,lettuce and tomato'
string[3:] 从第三个到最后，包含第三个
string[:3] 从第一个到第三个，不包含第三个
string[3:8] 前闭后开。
