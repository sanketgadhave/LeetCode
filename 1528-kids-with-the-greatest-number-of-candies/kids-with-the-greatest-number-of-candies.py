class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output_result = []
        for i in range(0, len(candies)):
            if candies[i]+extraCandies >= max(candies):
                output_result.append(True)
            else:
                output_result.append(False)

        return output_result