# "[1]:新增名片 "
card_list = []


def new_card():
    """
    新建名片函数
    :return:
    """
    while True:
        # pass
        print("请输入需要添加的信息")
        name = input("请输入需要添加的姓名：")
        phone = input("请输入需要添加的电话号码：")
        qq = input("请输入需要添加的qq号码：")
        email = input("请输入需要添加的邮箱：")
        card_dict = {"name": name,
                     "phone": phone,
                     "qq": qq,
                     "email": email}
        card_list.append(card_dict)
        print("添加信息成功！")
        print("请选择下一步操作\n "
              "[回车]:继续添加新的名片\n"
              "[其它任意按键]:退出添加新名片系统:")
        the_next = input("")
        if the_next == "" \
                       "":
            continue
        else:
            break


# "[2]:显示全部 "

def show_all_card():
    """
    此函数可以显示出所有已经记录的名片信息
    :return:
    """
    # pass
    if len(card_list) == 0:
        print("没有录入任何信息！")
    else:
        print("="*50)
        print("姓名\t电话\tqq\t邮箱\t")
        for card_dict in card_list:
            print("%s\t%s\t%s\t%s\t"% (card_dict ["name"],
                                       card_dict["phone"],
                                       card_dict["qq"],
                                       card_dict["email"]))
        print("="*50)

# "[3]:搜索名片 "


def search_card():
    """
    这是一个搜索函数，输入需要搜索的关键字，
    此函数可以给出关键字对应的信息，
    根据系统提示还可以对搜索到的信息进行修改、删除
    :return:
    """
    print("请输入需要搜索的姓名:")
    search_name = input("")
    for card_dict in card_list:
        if card_dict["name"] == search_name:
            print("=" * 50)
            print("姓名\t\t电话\t\tqq\t\t邮箱\t\t")

            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
            print("=" * 50)
            deal_search_name(card_dict)
            break

    else:
        print("没有找到%s的名片" % search_name)

    # pass


def deal_search_name(card_dict1):
    """
    这是一个处理函数，可以对形參传入的数据进行修改或者删除

    :param card_dict1:形參变量
    :return:
    """
    # print(search_name1)
    while True:
        input_key = input("请输入您要进行的操作  "
                          "[1]:修改 "
                          "[2]: 删除"
                          "[0]:返回上级菜单:")

        # pass
        # 修改
        if input_key == "1":
            # card_dict1["name"] = input("请输入需要修改的姓名: ")
            # card_dict1["phone"] = input("请输入需要修改的电话号码: ")
            # card_dict1["qq"] = input("请输入需要修改的qq: ")
            # card_dict1["email"] = input("请输入需要修改的email: ")

            card_dict1["name"] = new_input(card_dict1["name"], "请输入需要修改的姓名: ")
            card_dict1["phone"] = new_input(card_dict1["phone"], "请输入需要修改的电话号码: ")
            card_dict1["qq"] = new_input(card_dict1["qq"], "请输入需要修改的qq: ")
            card_dict1["email"] = new_input(card_dict1["email"], "请输入需要修改的email: ")
            print("修改成功！")
            break
        # 删除

        elif input_key == "2":
            card_list.remove(card_dict1)
            print("删除成功！")
            break

        else:
            break


def new_input(original_value, tip_message):
    """定义啦一个新的输入函数
    当有输入值的时候返回当前输入值
    当没有输入值的时候返回原来的值

    :param original_value:原来的值
    :param tip_message:提示信息
    :return: 返回函数
    """
    print(tip_message)
    new_word = input()
    if new_word == "" \
                   "":
        return original_value
    else:

        return new_word


