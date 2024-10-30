print("bag" > "apple")
print("bag" == "BAG")
print(ord("b"))
print(ord("B"))


tem = 21
if tem > 30:
    print("its>30")
elif tem > 20:
    print("its>20")
else:
    print("its else")
print("done")


age = 13
message = "yes"if age > 12 else "no"
print(message)

h = True
w = False
if h or w:
    print("1")
else:
    print("2")

# for 循环
for number in range(3):  # 从0开始，到2
    print("qqq", number, number+1, (number+1)*".")

for number in range(1, 4):  # 左闭右开
    print("qqq", number, number*".")

for number in range(1, 10, 2):  # 2为步数
    print("qqq", number, number*".")

sss = True
for number in range(3):
    if sss:
        print("sss")
else:  # else指的是循环正常结束后要执行的代码，即如果是bresk终止循环的情况。else下方缩进的代码将不执行。
    print("fff")


sss = True
for number in range(3):
    if sss:
        print("sss")
        break
else:  # else指的是循环正常结束后要执行的代码，即如果是bresk终止循环的情况。else下方缩进的代码将不执行。
    print("fff")


for x in range(3):
    for y in range(2):
        print(f"({x},{y})")


print(type(5))  # int
print(type(range(5)))  # range

for x in "lining":  # in后面需要一个复杂类型
    print(x)
for x in [1, 2, 3, 4]:
    print(x)

command = ""
# while command != "quit" and command != "QUIT":
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
