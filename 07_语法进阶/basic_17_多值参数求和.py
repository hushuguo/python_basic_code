# def sum_n(nums):
def sum_n(*nums):
    value = 0
    for num in nums:
        value += num
    return value


# r = sum_n((1, 2, 3, 4, 5))
r = sum_n(1, 2, 3, 4, 5)
print(r)
