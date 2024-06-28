def maxWater(arr) -> int:
    left = 0
    right = len(arr) - 1

    lmax = arr[left]
    rmax = arr[right]

    result = 0

    while left < right:
        if lmax < rmax:
            left += 1
            lmax = max(lmax, arr[left])
            result += lmax - arr[left]
        else:
            right -= 1
            rmax = max(rmax, arr[right])
            result += rmax - arr[right]

    return result


if __name__ == '__main__':
    arr = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    print(maxWater(arr))
