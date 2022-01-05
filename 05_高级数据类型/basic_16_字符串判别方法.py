# 判断空白字符
space_string = "  \t\n\r"
print(space_string.isspace())

# 判断字符串中只包含数字
# num_str = "\u00b2"
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

