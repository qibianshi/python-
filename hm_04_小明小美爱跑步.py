class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s的体重是%.2f" % \
               (self.name, self.weight)

    def run(self):
        print("%s爱跑步，跑步能减肥！" % self.name)
        self.weight -= 1

    def eat(self):
        print("%s是个吃货" % self.name)
        self.weight += 1


tom = Person("小美", 45)
tom.eat()
tom.run()
print(tom)

jerry = Person("小明", 75)
jerry.eat()
jerry.run()
print(jerry)

