def print_line(char, num):
    """打印分割线"""
    print(char * num)


def print_line_row(char, num, row):
    """打印多行分割线

    :param char: 分割线使用的分隔符
    :param num: 分隔符的个数
    :param row: 分割线的行数
    """
    i = 0
    while i < row:
        i += 1
        print_line(char, num)


print_line_row("-", 50, 5)
