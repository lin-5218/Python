import math
a = "qwe123456"
print(len(a))
print(a[0])
print(a[-1])   # 最后一个
print(a[0:3])  # 某几个
print(a[0:])   # 全部
print(a[:3])   # 0-3
print(a[:])   # 全部

# 逃逸字符
abc = "qqq\'www"
print(abc)
abc = "qqq\\www"
print(abc)
abc = "qqq\nwww"
print(abc)

f = "li"
s = "ning"
full = f+" "+s
full = f"{f} {s}"  # f"{a} {b}" ="a b" 里面相当于一个表达式
print(full)
full = f"{len(f)} {321}"
print(full)


abc = " li Ning "
print(abc)
print(abc.upper())  # 大写
print(abc.lower())  # 小写
print(abc.title())  # 标题格式
print(abc.strip())  # 去掉两侧的空格
print(abc.rstrip())  # 去掉右侧的空格
print(abc.lstrip())  # 去掉左侧的空格
print(abc.find("Nii"))  # 不存在返回-1
print(abc.replace("N", "K"))  # 替换
print("Nii" in abc)  # 返回bool
print("Nii" not in abc)  # 返回bool


print(10/3)
print(10//3)  # 两个数相除，结果为向下取整的整数
print(10*3)
print(10**3)  # 幂运算


print(round(2.9))  # 四舍五入
print(abs(-2.9))  # 绝对值


print(math.ceil(2.2))  # 向无穷大取整


x = input("x: ")  # 输入默认为字符串，需要进行类型转换，int(x),float(x),bool(x),str(x)
print(type(x))
y = int(x)+1
print(f"x:{x},y:{y}")


# bool有三种类型，True，False，None
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(""))
print(bool(" "))

c = 1+2j
print(type(c))
