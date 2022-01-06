class Cat:

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


# 创建猫对象
tom = Cat()
# 对象增加属性
tom.name = "Tom"

tom.eat()
tom.drink()
print(tom)


# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
