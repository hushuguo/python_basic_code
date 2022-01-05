import random
hand = int(input("请输入石头剪刀布，石头（1），剪刀（2），布（3）："))
computer = random.randint(1, 3)
print("玩家选择的是%d,电脑出的是%d" % (hand, computer))

if (hand + 1) % 3 == computer:
    print("玩家胜利")
elif hand == computer:
    print("平局")
else:
    print("玩家失败")
