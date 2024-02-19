class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        output_count = 0
        for ch in s:
            for j in range(count, len(t)):
                if ch == t[j]:
                    output_count += 1
                    count = j+1
                    break
            
        if output_count == len(s):
            return True
        else:
            return False
                