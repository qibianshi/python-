class Gun:
    def __init__(self, model):
        self.model = model
        self.count = 0
        self.fire_count = 0
        self.remain_count = 0

    # def __str__(self):
    #     return (("枪支型号为：%s\n"
    #              "装填子弹数为%d\n"
    #              "开火次数为%d\n"
    #              "剩余子弹为%d\n") %
    #             (self.model,
    #              self.count,
    #              self.fire_count,
    #              self.remain_count))

    def add_bullet(self, count):
        self.count = count + self.count
        print("[%s]装填子弹数为:%d\n剩余子弹为:%d\n" %
              (self.model, count, self.count))

    def shoot(self, fire_count):
        self.fire_count = fire_count
        if self.fire_count > self.count:
            self.fire_count = self.count
            print("[%s]子弹不够,开火次数为%s" % (self.model, self.count))
            return
        else:
            self.remain_count = self.count - self.fire_count
            print("[%s]开火次数为%s\n剩余子弹为%s" %
                  (self.model, self.fire_count, self.remain_count))


class Solider:
    def __init__(self, name):
        self.name = name
        self.gun_name = None

    # def __str__(self):
    #     return ("士兵%s 有一把%s"
    #             % (self.name, self.gun_name))

    def gun(self):
        if self.gun_name is None:
            print("[%s]没有枪！" % self.name)
        print("[%s]有一把[%s]" % (self.name, self.gun_name))
        self.gun_name.add_bullet(100)
        self.gun_name.shoot(50)


ak47 = Gun("AK47")

an = Solider("An")
an.gun_name = ak47
# an.gun_name.add_bullet(100)
# ak47.shoot(50)
an.gun()
# print(an.gun())
