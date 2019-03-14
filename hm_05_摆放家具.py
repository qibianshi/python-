class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return ("[%s] 占地面积：%.2f" %
                (self.name, self.area))


class House:
    def __init__(self, house_type, house_area):
        self.house_type = house_type
        self.area = house_area
        self.free_area = house_area
        self.item_list = []

    def __str__(self):
        return ("房子类型为：%s\n"
                "房子面积为：%.2f\n"
                "剩余面积为：%.2f\n"
                "已经添加的家具有：%s\n"
                % (self.house_type,
                   self.area,
                   self.free_area,
                   self.item_list
                   ))

    def add_item(self, item):

        print("要添加%s" % item)

        if item.area > self.free_area:
            print("面积太大无法添加%s" % item)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


bad = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

# 添加对象
my_home = House("两室一厅", 120)
my_home.add_item(bad)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
