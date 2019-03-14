#! /usr/bin/python3

import hm_02_cards_tools

while True:
    print("*" * 50)
    print("*" * 50)

    input_str = input("请输入您要进行的操作\n "
                      "[1]:新增名片\n "
                      "[2]:显示全部\n "
                      "[3]:搜索名片\n "
                      "[0]:退出系统:")
    print("您选择的操作是:%s" % input_str)

    if input_str in ["1", "2", "3"]:

        # "[1]:新增名片 "
        if input_str == "1":
            hm_02_cards_tools.new_card()

        # "[2]:显示全部 "
        if input_str == "2":
            hm_02_cards_tools.show_all_card()

        # "[3]:搜索名片 "
        if input_str == "3":

            hm_02_cards_tools.search_card()

        # pass
    elif input_str == "0":
        # [0]退出系统
        break
        # pass
    else:
        print("您输入的信息有误，请重新输入！")


print("欢迎再次使用[名片管理系统]")
