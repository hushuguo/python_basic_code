class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()

print(tom)
# 引用也适用于面向对象
addr = id(tom)
print("%x" % addr)
