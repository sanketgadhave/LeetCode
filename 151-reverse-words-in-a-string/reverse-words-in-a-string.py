class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = list(s.split())
        word_list.reverse()
        output_str = ' '.join([str(word) for word in word_list])

        return output_str