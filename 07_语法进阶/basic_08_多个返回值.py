def measure():
    """测量温度和湿度"""
    print("测量开始……")
    temp = 39
    wetness = 50
    print("测量结束……")

    # 利用元组可以返回多个数据
    return temp, wetness


result = measure()
print(result[0])
print(result[1])

gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)