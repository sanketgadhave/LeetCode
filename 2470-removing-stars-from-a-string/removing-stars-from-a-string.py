class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if i == '*':
                st.pop()
            else:
                st.append(i)
            
        return ''.join(c for c in st)