def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
    result = "hello"
    print("函数要返回的内存地址是%d" % id(result))
    return result


a = 10
print("a 保存的数据内存的地址是 %d" % id(a))
# 如果函数有返回值，但是没有定义变量接收，无法获得返回结果
r = test(a)
print("%s 的内存地址是 %d" % (r, id(r)))