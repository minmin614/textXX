"""
现在又10个学生的成绩，需录入系统中
这个人分别是，张三，李四，王麻子，浪晋，刘云，嘻嘻，小梁，小小，二狗，小猪
成绩和名字对上
大于60和小于60分开存放

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

hcj={}
lcj={}
student=["张三","李四","王麻子","浪晋","刘云","嘻嘻","小梁","小小","二狗","小猪"]
a=0
for i in student:
    chengji=int(input("请输入"+i+"的成绩："))
    if chengji>=60:
        hcj[i]=chengji
    else:
        lcj[i]=chengji

    a=a+1
    print("大于60的：",hcj)
    print("小于60的：",lcj)
"""
"""
       九九乘法表
       1*1
       1*2 2*2
"""
"""    
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end="  ")
    print()
"""
"""
 练习1：
  通过print打印，模拟一个红绿灯功能，注意红灯30次，绿灯35次，黄灯3次
  i=30
while i>0:
    print("红灯还有", i ,"秒")
    i=i-1
j=35
while j>0:
    print("绿灯还有", j ,"秒")
    j=j-1
for t in range(3):
    print(t)

练习2
 使用代码，实习注册功能
 用户输入账号密码，要求账号长度是5——8位，密码6——12位，并且账号必须小写开头
 储存到字典中 username：password
"""
"""
light={"红灯":30,"绿灯":35,"黄灯":3}
for i in light:
    for j in range(light[i]):
        #print(i,j)
        print(i,light[i]-j)
"""
username=input("请输入账号：")
password=input("请输入密码：")
if len(username)>=5 and  len(username)<=8:
    if username[0] in "abcdefghijklmnopqrstuvwxyz":
        if  len(password)>=5 and len(password)<=8:
            print("注册成功！",{username:password})
        else:
            print("密码必须8-12位")
    else:
        print("账号必须小写字母开头")
else:
    print("账号必须5-8位")