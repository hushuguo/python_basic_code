xiaoming_dict = {"name": "xiaoming"}
# 取值
print(xiaoming_dict["name"])
# print(xiaoming_dict["name123"])

# 增加/修改
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = "小小明"
# 删除
xiaoming_dict.pop("name")
print(xiaoming_dict)
