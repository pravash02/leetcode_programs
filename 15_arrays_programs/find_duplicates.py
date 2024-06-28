def duplicates(arr):
    freq_map = {}
    result = []

    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    for key, value in freq_map.items():
        if value > 1:
            result.append(key)

    if not result:
        result.append(-1)

    result.sort()
    return result


if __name__ == "__main__":
    a = [1, 6, 5, 2, 3, 3, 2]
    duplicates_found = duplicates(a)

    print("Duplicate elements:", end=" ")
    for element in duplicates_found:
        print(element, end=" ")
    print()
