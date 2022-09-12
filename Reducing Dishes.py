def multSum(A):
    """
    It takes an array of integers, multiplies each integer by its index+1 (unit of time), and returns the sum of all the products

    :param A: an array of integers
    :return: The sum of the multiplication of the index+1 and the value of the index.
    """
    sum = 0  # Initialize sum to be 0
    length = len(A)  # Length of array A

    # Loop from 0 to A length
    for time in range(length):
        sum += ((time + 1) * A[time])  # Multiplication of each item with its index+1

    return sum


class Solution(object):

    def maxSatisfaction(self, satisfaction):
        """
        "We sort the array, and then we iterate from the end to the start
        and check if the sum of the current index is greater than the sum of the previous index. If so, we keep iterating,
        and if not, we stop and return the maximum sum."

        :param satisfaction: The array of satisfaction values
        :return: The maximum sum of the satisfaction array
        """

        # =======================================================================================================

        # Parameters declarations
        length = len(satisfaction)  # Length of satisfaction array
        index = length - 1  # the index at the last position
        sum = 0  # Initialize sum to be 0
        max = 0  # initialize max to be 0

        # =======================================================================================================

        # Sort the input array
        satisfaction.sort()

        # =======================================================================================================

        # Worst case: All items <= 0, hence 'People do not like the dishes. No dish is prepared.' and return 0
        if satisfaction[-1] <= 0:
            return 0

        # =======================================================================================================

        # Best case: All items are >=0 (and array not including only 0 - In the previous step was the checking)
        elif satisfaction[0] >= 0:
            for i in range(length):
                sum += (i + 1) * satisfaction[i]

            return sum
        # =======================================================================================================

        # There both positive, negative and might be 0 in the array and the goal is to maximize the problem
        # After array sorting, we try to scan the array from the end to the start (from the biggest number to the smallest
        # one), and in each time we compare the last k index compared to the k+1 index and check if the sum of the k+1 index
        # is greater than the sum of the k index. if so, keep scaning, and if not stop and return the maximum sum.
        # At the point the sum start to decrease, it will decrease also for the next item so the algorithm stop at
        # this point.

        else:
            while index >= 0:  # Loop from the last index to the first one
                current_sum = multSum(satisfaction[index:length])  # The sum until the current index
                if current_sum < max:  # in case that we found the max sum through the iteration
                    break
                else:
                    max = current_sum  # Update the max sum
                index -= 1  # Iterate the array index

            return max