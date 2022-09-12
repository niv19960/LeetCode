def initMatrix(len1, len2):
    # initialize all matrix to 0 values
    mat = [[0] * len2 for _ in range(len1)]

    # initialize the first col to its index
    for i in range(len1):
        mat[i][0] = i

    # initialize the first row to its index
    for i in range(len2):
        mat[0][i] = i

    return mat


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        # Using dynamic programming
        matrix = initMatrix(len1 + 1, len2 + 1)

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # two characters are identical - nothing to change
                if word1[i - 1] == word2[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                # check which operation is the cheapest (insert, delete, replace)
                else:
                    upper_element = matrix[i - 1][j]  # Remove
                    left_element = matrix[i][j - 1]  # Insert
                    upper_left_elemnt = matrix[i - 1][j - 1]  # Replace

                    # We want the lower cost operation until the current substring
                    matrix[i][j] = 1 + min(upper_element, left_element, upper_left_elemnt)

        # bottom right index will represent the number of operations
        return matrix[-1][-1]

