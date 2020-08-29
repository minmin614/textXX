"""
print("hello world!")
print(2333)
print(2.333)
print(True)
print(()) #元组
print([]) #数组
print({}) #字典
print("hhah")
print("haha"*100)
print(1+2)
a=float(input("请输入："))
b=float(input("请输入："))
print("input获取的内容:",a+b)

c=type()
print(type("哈哈"))

#a=float(len(input("请输入:")))
#b=float(len(input("请输入:")))
#print("input获取的内容:",a+b)
#元组,下标，从0开始编号
a=(1,2,3,4,"哈哈","嘻嘻" ,False,1,1,1,4)
#print(a)
#print(a[2])
#print(a.index("哈哈"))
#print(a.count(1))

#二维元组
#b=(a,"haha","xixi")
#print(b[0][3])
#print(a[-1])
# 切片
print(a[0:4]) #左闭右开 不写就是开始或者结束
print(a[:4])
print(a[3:])

a=[1,2,3,4,"哈哈","嘻嘻" ,False,1,1,1,4]
a.append("append1")
a.append("tam")
a.insert(0,"insert")
a.insert(3,"key")


#元组一旦写好后不可以修改，数组可以修改
b=a.pop(5) #剪切
c=a.pop(2)
print(c)
#print(b+c)
#d=a.clear()
#print(d)
xx=["1","2"]
a.extend(xx)
print(a+xx)
a.remove(0)
print(a)
#tru=1 false=0 下标不要超出范围

# 所有的方法都是小括号结尾 print()
 #元组数组字典的取值，都是中括号 a[]
 #元组数组字典的定义分别是()[]{}


# 字典的特点

 1、字典中的值没有顺序
 2、字典的结构必须是键值对的结构 ，key:value
 3、字典的取值都是通过key去取值

"""
"""
a={ "name":"张三",0:"哈哈", "age":25}
#取值
print(a["name"])

#新增
a["high"]="183cm"
print(a)
#修改
a["name"]="李四"
print(a)

b=a.get("name")
print(b)
b=a.pop("name")
print(b)
print(a)

a.update(name ="哈哈")
print(a)
print("--------------------")
print(a.get("name"))
print(a["name"])

#数组和字典的删除
del a["name"]
print(a)
"""

#练习：获取用户输入个人信息，并且存在字典中
#个人信息包含了，name，age，sex

print("-----------------------")
a =input("输入用户名:")
b=input("请输入年龄:")
c =input("请输入性别:")
#print(a)
#print(b)
#print(c)
#inform={"name":a,"age":b,"sex":c}
inform ={}
inform.update(name=a,age=b,sex=c)

print(inform)

