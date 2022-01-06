def sum_numbers(num):
    """数字累加的普通方法
    :param num: 从num开始求和
    :return:
    """
    sum_recur = 0
    while num > 0:
        sum_recur = num + sum_recur
        num -= 1
    return sum_recur


r = sum_numbers(3)
print(r)


def sum_num_recur(num):
    if num == 1:
        return 1
    temp = sum_num_recur(num - 1)
    return temp + num


result = sum_num_recur(100)
print(result)
