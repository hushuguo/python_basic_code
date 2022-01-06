a = (1, 2, 3, 4, 5)
b = (-1, -2, -3, -4, 6)


def demo(tuple1, tuple2):
    i = 0
    c = []
    while True:
        if tuple1[i] * tuple2[i] < 0:
            c.append(0)
        else:
            c.append(1)
        if i == len(a) - 1:
            break
        i += 1
    return c


r = demo(a, b)
print(r)
