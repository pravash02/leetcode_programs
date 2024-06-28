def findFreeinterval(arr, N):
    if N < 1:
        return

    stack = []

    arr.sort(key=lambda x: x[0])
    stack.append(arr[0])

    for i in range(1, len(arr)):
        prev_ind = stack[-1][-1]
        curr_ind = arr[i][0]

        if prev_ind >= curr_ind:
            stack[-1][-1] = max(stack[-1][-1], arr[i][1])
        else:
            stack.append(arr[i])

        print(arr, stack)

    return stack


# arr = [[1, 3], [2, 4], [3, 5], [7, 9]]
# arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
arr = [[1, 3], [2, 4], [6, 8], [9, 10]]
N = len(arr)
print(findFreeinterval(arr, N))
