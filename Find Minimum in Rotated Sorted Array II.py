class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        # low, high, mid - refering to the index value

        while low < high:
            mid = (low + high) // 2

            # the minimum locate at the right to the mid - array is not sorted
            if nums[mid] > nums[high]:
                low = mid + 1

            # the minimum locate at the left to the mid - array is not sorted
            elif nums[low] > nums[mid]:
                high = mid
                low += 1

            # nums[low] <= nums[mid] <= nums[high]  - The array is sorted between low and high (including duplicted numbers)
            else:
                high -= 1

        return nums[low]  # minimum value