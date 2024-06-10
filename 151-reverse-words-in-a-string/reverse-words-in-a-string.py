class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        word_list.reverse()
        word_list = [word for word in word_list if word.strip()]
        return ' '.join(word_list)
