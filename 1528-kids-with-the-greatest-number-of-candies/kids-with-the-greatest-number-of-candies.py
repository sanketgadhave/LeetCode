class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        final = [False for i in range(len(candies))]
        max_num = max(candies)
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= max_num:
                final[i] = True

        return final