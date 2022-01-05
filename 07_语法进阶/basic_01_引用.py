def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))


a = 10
print("a 保存的数据内存的地址是 %d" % id(a))
test(a)
