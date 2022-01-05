hello_str = "hello world"

# 1.判断字符串是否以指定字符开始
print(hello_str.startswith("hel"))

# 2.判断字符串是否以指定字符结束
print(hello_str.endswith("rld"))

# 3.查找指定字符串
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# 4.替换字符串
print(hello_str.replace("world", "hello"))