def candies_array(ratings):
    candies = [0] * len(ratings)  # initialize array of candies (each index represent a different child)
    candies[0] = 1  # initialize first child to have one candy (the constrain of at leat one candy per child)

    for i in range(1, len(ratings)):
        # the right child has lower or equal rating than the left one, so he can get one candy
        if ratings[i] <= ratings[i - 1]:
            candies[i] = 1
        # the right child has higher rating than the left one, so he can get one more candy than the left one
        elif ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    return candies


class Solution:
    def candy(self, ratings: List[int]) -> int:

        # One child
        if len(ratings) == 1:
            return 1
        # Because we have to consider in both neighbors of each child, wh once calculate the number of candies from the left child to the right one,
        # and second time we calculate in the opposite way
        l2r = candies_array(ratings)  # calculate from left to right
        ratings.reverse()  # calculate from left to right
        r2l = candies_array(ratings)
        r2l.reverse()  # return reverse array to the original one

        sum_of_candies = 0

        # We have two possiblities to give candies
        # Because we have to consider in neighbors of each child, we take the maximu, value from those two arrays of candies calculation
        for i in range(0, len(ratings)):
            sum_of_candies += max(l2r[i], r2l[i])

        return sum_of_candies  # return the number of candies