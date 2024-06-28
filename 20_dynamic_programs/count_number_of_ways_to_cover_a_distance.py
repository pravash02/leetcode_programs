def printCountDP(dist):
    count = [0] * (dist + 1)
    print(count)

    # Initialize base values. There is one way to cover 0 and 1 distances and two ways to cover 2 distance
    count[0] = 1
    if dist >= 1:
        count[1] = 1
    if dist >= 2:
        count[2] = 2

    print(count)

    # Fill the count array in bottom up manner
    for i in range(3, dist + 1):
        print(count[i - 1], count[i - 2], count[i - 3])
        count[i] = count[i - 1] + count[i - 2] + count[i - 3]
        print(count)

    return count[dist]


# driver program
dist = 6
print(printCountDP(dist))
