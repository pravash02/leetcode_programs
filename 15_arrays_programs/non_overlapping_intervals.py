def findFreeinterval(arr, N):
    if N < 1:
        return

    P = []

    arr.sort(key=lambda a: a[0])

    for i in range(1, N):
        prevEnd = arr[i - 1][1]
        currStart = arr[i][0]

        if prevEnd < currStart:
            P.append([prevEnd, currStart])

    for i in P:
        print(i)


arr = [[1, 3], [2, 4], [3, 5], [7, 9]]
N = len(arr)
findFreeinterval(arr, N)
