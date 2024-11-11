class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag = -1
        count = 0
        for i in range(len(s)):
            for j in range(flag+1, len(t)):
                if s[i] == t[j]:
                    flag = j
                    count +=1
                    break
        
        if count == len(s):
            return True
        else:
            return False