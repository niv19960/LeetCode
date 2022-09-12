import functools


def xor(num1, num2):
    """
        The function xor takes two numbers as input and returns the result of the bitwise XOR operation on those numbers.

        :param num1: The first number to be in the XOR opreation
        :param num2: The second number to be used in the XOR operation
        :return: The result of the operation.
        """
    result = num1 ^ num2
    return result


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
            It takes two arrays and returns the AND of the XORs of the arrays

            :param arr1: array of integers
            :param arr2: array of integers
            :return: The AND between the XOR of the two arrays.
            """

        # reduce: take an array and apply xor on each adjacent pair of items until scannig all the array.
        # return type: int
        xor_arr1 = functools.reduce(xor, arr1)
        xor_arr2 = functools.reduce(xor, arr2)

        # calculate AND between both XOR results of the arrays
        and_arr1_arr2 = xor_arr1 & xor_arr2

        return and_arr1_arr2

