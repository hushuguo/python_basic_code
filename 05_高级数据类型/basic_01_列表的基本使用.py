name_list = ["zhangsan", "wangwu", "lisi"]

# 取值和取索引
print(name_list[0])

print(name_list.index("lisi"))

# 修改
name_list[1] = 'lisi'
# name_list[3] = "wangxiaoer"

# 增加
name_list.append("wangxiaoer")

name_list.insert(2, "xiaomeimei")

temp_list = ["孙悟空", "沙师弟", "猪八戒"]
name_list.extend(temp_list)

# 删除
name_list.remove("lisi")

name_list.pop()
name_list.pop(3)

name_list.clear()

print(name_list)