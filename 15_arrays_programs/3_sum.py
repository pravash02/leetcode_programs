from typing import List


def find_triplet(arr):
    arr.sort()
    N = len(arr)
    l = []
    for i in range(N - 2):
        if arr[i] + arr[i + 1] + arr[i + 2] == 0:
            print(arr[i], arr[i + 1], arr[i + 2])
            l.append([arr[i], arr[i + 1], arr[i + 2]])


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        # Skip duplicate elements to avoid repeating triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1

        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]

            if current_sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                # skip duplicates for 2nd
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

                # skip duplicates for 3rd
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

            elif current_sum < 0:
                l += 1
            else:
                r -= 1

    return result


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    # find_triplet(arr)
    print(threeSum(arr))
