"""
#python语句
#if条件语句
a=20
if a>18:
    print("成年人")
else:
    print("未成年")
#字符串条件 in，判断某个字符串是否在另外一个字符串中
t="你两还争风吃醋上了"
y="争风吃醋"
if y in t:
    print("y在t中")
else:
    print("不在")
# == 判断
# = 赋值
# ！= 不等于
b=123
c=1234
if b==c:
    print("b=c")
else:
    print("b!=c")
"""
#练习：输入一个数字，来判断数字的大小，如果这个数字大于18:，则打印 "黄花大闺女";否则打印“钢铁直男”。
# a=int(input("请输入一个数字："))
# if a>18:
#     print("黄花大闺女")
# else:
#     print("钢铁直男")

# #进阶版的：请输入一个字符串，判断字符串的长度大于6个字，如果大于就打印输入的内容合格。否则就显示不合格。
# b=input("请输入字符串：")
# if len(b)>6:
#     print("输入内容合格")
# else:
#     print("输入不合格")

#多条件 and or 
# name=input("请输入字符串")
# if name=="大雁塔" and len(name)==3:
#     print("对了")
# else:
#     print("错了")
# if 嵌套
# name=input("请输入字符串")
# if name=="大雁塔":
#     if len(name)==3:
#         print("对了")
#     else:
#         print("错了")
# else:
#     print("错了")
# a=30
# if a>18:
#     print("成年人")
# elif a>16:
#     print("青年小伙伴")
# elif a>14:
#     print("少年小伙伴")
# elif a>6:
#     print("少先队员")
# else:
#     print(XXX)

# 作业：
# 1. 把代码用vscode抄三遍  （基础）
# 进阶：
# 2.输入一个账号，输入一个密码，要求判断账号的长度大于5位，并且小于8位，
# 如果输入账号为张三12345，密码为123456就可以登录成功，否则就登录失败
a=input("请输入账号：")

if len(a)>5 and len(a)<8:
    if a =="张三12345":
        b=input("请输入密码")
        if b =="123456":
            print("登录成功")
        else:
            print("登录失败")
    else:
        print("账号错误")
else:
    print("账号不满足要求")


