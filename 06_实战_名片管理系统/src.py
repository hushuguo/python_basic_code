# 用来保存名片的字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """添加名片"""
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    # shift + F6
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱:")
    # 2.使用用户输入的信息建立字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str
                 }
    # 3.将字典加入到列表中
    card_list.append(card_dict)
    # 4.提示添加成功
    print("%s的信息添加成功" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    # 如果为空
    if len(card_list) == 0:
        print("当前无记录，请添加记录")
        return
    # 打印表头
    for name in ["姓名", "电话", "qq号", "邮箱"]:
        print(name, end="\t\t")
    # 打印分割线
    print("")
    print("=" * 50)
    for card_info in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_info["name"],
                                        card_info["phone"],
                                        card_info["qq"],
                                        card_info["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入你要查找的姓名:")
    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for info_dict in card_list:
        if info_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (info_dict["name"],
                                            info_dict["phone"],
                                            info_dict["qq"],
                                            info_dict["email"]))
            deal_card(info_dict)
            break
    else:
        print("没找到%s的信息" % find_name)


def deal_card(find_dict):
    """处理查找到的名片
    :param find_dict: 查找到的个人字典
    """
    print(find_dict)
    while True:
        action_str = input("请选择要执行的操作: 1.修改 2.删除 0.返回上级菜单")
        if action_str == "1":
            find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名：【回车不修改】]")
            find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话：【回车不修改】")
            find_dict["qq"] = input_card_info(find_dict["qq"], "请输入qq：【回车不修改】")
            find_dict["email"] = input_card_info(find_dict["email"], "请输入邮箱:【回车不修改】")
            break
        elif action_str == "2":
            card_list.remove(find_dict)
            print("删除名片成功")
            break
        elif action_str == "0":
            break
        else:
            print("输入错误，请重新输入")


def input_card_info(dict_value, tip_message):
    """在修改名片的时候，不输入不修改，输入修改
    :param dict_value:寻找到的字典中的各项值（name,phone，et）
    :param tip_message:修改的输入内容，用来返回
    :return:返回值为字典中各项的单独值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户不输入内容，返回字典中原有的值
    else:
        return dict_value
