# -*- coding: utf-8 -*-
__author__ = 'YSC-wangsh'

f = open('test.txt', 'w')
f.write("1.hello\n")
f.close()

# 追加文件
f = open('test.txt', 'a')
f.write("2.hello\n")
f.write("3.hello\n")
f.write("4.hello\n")
f.write("5.hello\n")
f.write("6.hello\n")
f.write("7.hello\n")
f.write("8.hello\n")
f.write("9.hello\n")
f.write("10.hello\n")
f.close()

# 读取全部内容
f = open('test.txt', 'r')
text = f.read()
print(text)
f.close()


# 将文件内容读取并保存到一个list中并输出
i = 1
f = open('test.txt', 'r')
fileList = f.readlines()
for fileLine in fileList:
    print("第%d行：%s" %(i,fileLine))
    i += 1
    # print(fileLine)
f.close()


# 逐行读取文件，python会记录读取的位置
print("###################################")
f = open('test.txt', 'r')
fileList = f.readline()
fileList2 = f.readline()
print(fileList2)



