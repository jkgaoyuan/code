

#列表中的元素不限制类型,列表内容可读可修改
#定义
alits=["a","123","0.123"]
print(alits)
# print(alits[0])
# alits.append("monkey")
# print(alits)
# alits.insert(1,"only")
# del alits[0]
# len(alits)
# print(max(alits))
# print(min(alits))

# 元组中数据类型也不限制，之间用，分隔
# 元组中的数据只读不可修改
#当元组中只有一个 元素时需要在最后加上 ，
tup=('apple',123,'xiaomi')
print(tup)
print(tup[0])
print(tup.index('apple'))
# tup.index('apple')
# tup[:3]
# del tup

# 字典 存储kv 数值
# 键是唯一的，数值可以相同；字典不支持位置下标（如[0]）访问，仅支持键下标（如["name"]）访问； 如果需要通过下标访问则需要转换为列表
dict_a={"apple": "苹果", "banana":"香蕉"}
print(dict_a["apple"])
import matplotilb.pyplot as plt 
import matplotlib.pyplot