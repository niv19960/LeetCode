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
    def xorGame(self, nums: List[int]) -> bool:
        xor_result = functools.reduce(xor, nums) == 0  # The bitwise XOR of all the elements - True/False
        queue_result = (len(nums) % 2) == 0  # is nums of turns for Alice is even - True/False

        # First case: If any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins (Alice allways starts)
        # Second case: xor_result = 0 - assuming both players play optimally so Alice can control the game - she will never erase a number such as (a_k ^ rest of elemnts = 0) (in case that xor_result=0)
        if xor_result:
            return True

        # If (XOR result != 0) Alice depends on the number of turns and if she erase the last element she will lose
        return queue_result

