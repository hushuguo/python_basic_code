a = 6
b = 10
# 1.使用其他变量
c = a
a = b
b = c
print(a, b)

# 2.不使用其他的变量
a = a + b
b = a - b
a = a - b

# 3.python专有解法
a, b = b, a
print(a)
print(b)
