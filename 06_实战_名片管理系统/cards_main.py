#! /usr/bin/python3
# shebang的使用
import src

while True:
    src.show_menu()
    action_str = input("请选择希望执行的操作:")
    print("您选择的操作是【%s】" % action_str)

    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            src.new_card()
        # 显示全部
        elif action_str == "2":
            src.show_all()
        # 查询名片
        elif action_str == "3":
            src.search_card()
    elif action_str == "0":
        # 退出系统
        print("欢迎再次使用名片管理系统")
        break
        pass
    else:
        print("您输入的不正确，请重新选择")
