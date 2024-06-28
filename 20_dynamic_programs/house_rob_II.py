def rob(nums):
    return max(nums[0], calc(nums[1:]), calc(nums[:-1]))


def calc(nums):
    r1 = 0
    r2 = 0

    for i in nums:
        r1, r2 = r2, max(i + r1, r2)

    return r2


nums = [3, 4, 3]
print(rob(nums))
