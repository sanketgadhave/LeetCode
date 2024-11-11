class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0

        for i in range(0, len(s)-k+1):
            sub_st = s[i:k]
            count = sub_st.count('a') + sub_st.count('e') + sub_st.count('i') + sub_st.count('o') + sub_st.count('u')
            max_count = max(count, max_count)
            k+=1
        return max_count

