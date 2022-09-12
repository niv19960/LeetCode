def possibleSplitIntoMPieces(nums, limit, m):
    """
    Split the given array into k sub-arrays according to the limit sum. If k <= to the given m sub-arrays return True.
    Else return False.

    :param nums: the array of numbers
    :param limit: the maximum sum of any subarray
    :param m: the number of pieces we want to split the array into
    :return: True if k <= m, else False
    """

    subArrays_counter = 0  # k
    sum = 0  # current sum of any sub-array

    for num in nums:  # loop over all numbers in array

        if (sum + num) > limit:  # check if the sum of current sub-array is not bigger than limit
            # if True, update number of sub-arrays and update the sum to be the current number (it not includes in the
            # last sub-array because it goes over the limit)
            subArrays_counter += 1
            sum = num

        else:
            sum += num  # add current number to the current sum

    subArrays_counter += 1  # Cont the current sub-array (it not goes over the limit)
    if m >= subArrays_counter:  # return True if m >= k, else False
        return True
    else:
        return False


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        """
        We are trying to find the minimum value of the maximum sum of the subarrays

        :param nums: the array of numbers
        :param m: the number of pieces we want to split the array into
        :return: The minimum largest sum of any subarray.
        """

        high = sum(nums)  # the right boundary
        low = max(nums)  # the left boundary
        nums_length = len(nums)  # array length
        # result = 0  # initialized the result

        # checking the boundaries cases
        if m == nums_length:  # Each number is a sub-array
            return low
        if m == 1:  # All numbers include in one sub-array
            return high

        # Binary Search on the sum
        while low <= high:
            middle = (low + high) // 2

            # Succeed to divide the array into m sub-arrays
            # The minimum is found between low and middle
            if possibleSplitIntoMPieces(nums, middle, m):
                high = middle - 1
                result = middle

            # Unsuccessful to divide the array into m sub-arrays
            # The minimum is found between middle and high
            else:
                low = middle + 1

        return result