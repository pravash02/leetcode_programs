def maxArea(arr):
    l = 0

    r = len(arr) - 1

    area = 0

    while l < r:
        area = max(area, min(arr[l], arr[r]) * (r - l))

        if arr[l] < arr[r]:
            l += 1

        else:
            r -= 1

    return area


a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]

print(maxArea(a))
print(maxArea(b))
