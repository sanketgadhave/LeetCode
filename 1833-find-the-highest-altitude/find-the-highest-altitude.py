class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_list = [0]*(len(gain)+1)
        for i in range(len(gain)):
            prefix_list[i+1] = prefix_list[i]+gain[i]
        return max(prefix_list)