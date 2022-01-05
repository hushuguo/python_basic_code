student = [
    {"name": "小明",
     "age": "20",
     "gender": "male"
     },
    {"name": "小丽",
     "age": "18",
     "gender": "female"
     }
]
for stu_dic in student:
    if stu_dic["name"] == "小黄":
        print("列表里有小丽的信息:")
        break
else:
    print("没有找到小丽的信息")
