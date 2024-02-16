class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Initialize the left and right search boundaries at the beginning and end of the list
        low = 0
        high = len(nums) - 1

        # Continue the search until the left and right boundaries intersect
        while low <= high:
            # Set the mid pointer exactly in the middle between the left and right boundary
            mid = (low + high) // 2

            # If the number is found, return its index
            if nums[mid] == target:
                return mid

            # If the number on the left boundary is less than or equal to the middle,
            # then the left half is the sorted part of the list
            if nums[low] <= nums[mid]:
                # If the number is in this part, shift the right boundary to position mid,
                # trimming the right half of the list
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                # Otherwise, trim the left half of the list by shifting the right boundary to position mid
                else:
                    low = mid + 1
            # Otherwise, the right half will be sorted
            else:
                # If the number is in this part, shift the left boundary to position mid,
                # trimming the left half of the list
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                # Otherwise, trim the right half of the list by shifting the left boundary to position mid
                else:
                    high = mid - 1

        # If the number was not found throughout the entire loop, return -1
        return -1


srch = Solution()
print(srch.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
