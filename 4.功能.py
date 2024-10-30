# 函数定义

def fun1(x, y):
    print(f"{x}+{y}")


fun1("li", "ning")  # void
print(fun1("li", "ning"))  # void会默认返回none


def fun2(x, y):
    return f"{x}+{y}"


mess = fun2("li", "nnning")  # return
print(mess)
print(fun2("li", y="123"))  # 关键字

file = open("file1.txt", "w")  # 打开文件
file.write(mess)


def fun3(x, y=1):
    return f"{x}+{y}"


print(fun3(1, 4))


def fun4(*numbers):  # 所有参数以元组(tuple)的形式导入
    total = 1
    for num in numbers:
        total *= num
    print(total)


fun4(1, 2, 3)
l = [2, 34, 5]
print(type(l))
fun4(l)
fun4(*l)


def fun5(**mess):  # 将参数以字典的形式导入,类型结构体
    print(mess)
    print(mess["name"])


fun5(id=5, age="213", name="lining")


abc = "a"


def fun6(x):
    global abc  # 在函数中修改全局变量需要用global
    abc = "b"


fun6(2)
print(abc)


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbnuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"

    return input


print(fizz_buzz(5))
