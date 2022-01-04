name_list = ["张三", "李四", "王五", "张三"]
list_len = len(name_list)
print(list_len)

name_list.append("王小二")
list_len = len(name_list)
print(list_len)

count = name_list.count("张三")
print("张三出现了%d次" % count)
name_list.remove("张三")
print(name_list)