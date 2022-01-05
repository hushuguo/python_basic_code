poem = "\t\n登鹳雀楼\t王之涣\t白日依山尽\t\n黄河入海流\n欲穷千里目\t\t更上一层楼"
# 拆分字符串成列表
poem_list = poem.split()

# 合并列表
result = " ".join(poem_list)

print(result)