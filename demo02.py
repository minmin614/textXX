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
a=1
while a<10:
    print("哈哈哈",a)
    a=a+2

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