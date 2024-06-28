def rob(nums):
    r1 = 0
    r2 = 0

    for i in nums:
        temp = max(i + r1, r2)
        r1 = r2
        r2 = temp

    return r2


nums = [2, 9, 8, 3, 6]
print(rob(nums))
