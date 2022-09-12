# Extended Euclidean: d = gcd(a, b) = ax + by
# if all integers in array in gcd gives us 1 --> than exists combination of numbers in the array which gives us gcd=1 (this cobination is enough and we can multiple the rest of numbers by zero)
# if not the fcd of all numbers is another number from 1

import numpy as np


class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Find gcd of all array items
        result = np.gcd.reduce(nums)

        if result == 1:
            return True
        return False
