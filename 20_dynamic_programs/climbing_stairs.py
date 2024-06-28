def climbStairs(n):
    a = 1
    b = 1

    for i in range(n-1):
        temp = a + b
        a = b
        b = temp

    return b


n = 2
print(climbStairs(n))
