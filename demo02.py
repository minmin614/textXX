#判断
"""
a=1
b=2
if a>b:
    print("a比b大")
else:
    print("b比a大")
   
age=23
if age >60:
    print("退休了")
elif age>30:
    print("奋斗")
else:
    print("努力学习")


a="你好"
if a in "你好,111":
     print("111")
""" 
"""
    print("----------------------")
    a=10
    if type(a) is int:
        print("11")
    elif type(a) is str:
        print("22")
    else:
        print("33")
"""
#循环
"""
现在又10个学生的成绩，需录入系统中
这个人分别是，张三，李四，王麻子，浪晋，刘云，嘻嘻，小梁，小小，二狗，小猪
成绩和名字对上
大于60和小于60分开存放
"""
"""
hcj={}
lcj={}
student=["张三","李四","王麻子","浪晋","刘云","嘻嘻","小梁","小小","二狗","小猪"]
a=0
while a<len(student):
    chengji=int(input("请输入"+student[a]+"的成绩："))
    if chengji>=60:
        hcj[student[a]]=chengji
    else:
        lcj[student[a]]=chengji
    a=a+1
    print("大于60的：",hcj)
    print("小于60的：",lcj)
"""
# 遍历
"""
a=["张三","李四","王麻子","浪晋","刘云","嘻嘻","小梁","小小","二狗","小猪"]
for i  in a:
    print(i) 

b=list(range(0,100,3))  #自动生成一个数列 步进
print(b)
"""
#c=("嘿嘿","花花")
# b=("aaa","bbb","cccc","mmmm")
# a=(1,2,3,4,"哈哈","嘻嘻",True,None,b)
#少写几个变量
#每个变量都会占用内存，变量越多，占的越多
#下标就是计算机自动编号，正向从0开始,反向从-1开始
#print(a[4])
#print(a[-7]) None表示-1 true表示1
#print(a.index(4))
#print(a.count(1))
#二维元组，三维元组
#切片，左闭右开
# print(a[-2])
#print(a[-1][4][0]) 
# print(a[0:3])

b=("aaa","bbb","cccc","mmmm")
a=[1,2,3,4,"哈哈","嘻嘻",True,None,b]
#print(a)

# 元组和数组的操作方式一模一样
# 区别是元组不可以修改，数组可以修改
# name = input("请输入名字：")
# a.append(name)
# # print(a)
# a.insert(3,name)
# #print(a)
# xx=a.pop(8)
# print(xx)
# c=["o","p","q"]
# a.extend(c)
# print(a)

d=[1,3,4,5,2]
d.sort(reverse=False)
print(d)
