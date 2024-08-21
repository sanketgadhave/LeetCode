class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        flag = -1
        count = 0
        for i in range(len(s_list)):
            for j in range(flag+1, len(t_list)):
                if s_list[i] == t_list[j]:
                    flag = j
                    count+=1
                    break
        
        if count == len(s_list):
            return True
        else:
            return False