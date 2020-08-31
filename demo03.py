"""
字典没有下标的概念
说明了，字典没有顺序的说法
字典取值靠key
"""

a={"name":"张三","age":12} #key:value
#print(a["age"])
#取值
a["name"] #当key不存在时报错
a.get("name") #当key不存在时返回空值
#新增和修改
#a["address"]="成都" #当key不存在时，会新增，存在时即修改
# a.update(name="王二") #update的写法的时候，key在这里时一个变量的写法
# print(a)
# #取走
a.pop("name")
print(a)
# #删除 通用的删除方法，可以删字典
# del a["name"]

# print(list(a.values()))
