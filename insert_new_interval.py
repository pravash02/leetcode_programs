def insertinterval(arr, interval):
    stack = []

    arr.sort(key=lambda x: x[0])

    for i in range(1, len(arr)):
        if arr[i-1][1] < interval[0] or arr[i][1] >= interval[1]:
            arr.insert(i, interval)

    print(arr)

    stack.append(arr[0])

    for i in range(1, len(arr)):
        prev_ind = stack[-1][-1]
        curr_ind = arr[i][0]

        if prev_ind > curr_ind:
            stack[-1][-1] = max(stack[-1][-1], arr[i][1])
            stack[-1][0] = min(stack[-1][0], arr[i][0])
        else:
            stack.append(arr[i])

    return stack


# arr = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# interval = [4, 9]
arr = [[1, 3], [6, 9]]
interval = [2, 5]

print(insertinterval(arr, interval))
