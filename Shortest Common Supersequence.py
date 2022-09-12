def LCS(s1, s2):
    # https://www.geeksforgeeks.org/printing-longest-common-subsequence/
    # matrix_dimension = len(s) + 1 # To create additional first row and col of 0 values

    matrix = [[0 for col in range(len(s2) + 1)] for row in range(len(s1) + 1)]  # Fill all matrix values with 0 values

    # Implement LCS algorithm
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            elif matrix[i - 1][j] >= matrix[i][j - 1]:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i][j - 1]

    # Create a string variable to store the lcs string
    lcs = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = len(s1)
    j = len(s2)
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if s1[i - 1] == s2[j - 1]:
            lcs += s1[i - 1]
            i -= 1
            j -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # We traversed the table in reverse order
    # LCS is the reverse of what we got
    lcs = lcs[::-1]

    return lcs


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        lcs_string = LCS(str1, str2)

        i = 0  # iterate str1
        j = 0  # iterate str2

        result = ""  # the return variable, initialize at first to empty string

        for letter in lcs_string:  # iterate on each letter from the lcs_string

            # iterate over s1 until the current common letter
            while (str1[i] != letter):
                result += str1[i]
                i += 1

            # iterate over s2 until the current common letter
            while (str2[j] != letter):
                result += str2[j]
                j += 1

            result += letter  # concat the current common letter
            i += 1
            j += 1

        # concat the rest of s1 and s2 after scaning the lcs of s1 and s2
        result += str1[i:]
        result += str2[j:]

        return result
