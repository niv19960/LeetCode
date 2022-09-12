class Solution:
    def minInsertions(self, s: str) -> int:

        reverse_s = s[::-1]  # reverse s string

        str_length = len(s)
        matrix_dimension = len(s) + 1  # To create additional first row and col of 0 values

        matrix = [[0 for col in range(matrix_dimension)] for row in
                  range(matrix_dimension)]  # Fill all matrix values with 0 values

        # Implement LCS algorithm
        for i in range(1, matrix_dimension):
            for j in range(1, matrix_dimension):

                if s[i - 1] == reverse_s[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                elif matrix[i - 1][j] >= matrix[i][j - 1]:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i][j - 1]

        # return opposite result of LCS (the not common subsequence length)
        return str_length - matrix[-1][-1]
