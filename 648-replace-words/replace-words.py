class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary, key=len)
        sentence_list = sentence.split(" ")
        for i in range(len(sentence_list)):
            for root in dictionary:
                if sentence_list[i].startswith(root):
                    sentence_list[i] = root
                    break
                
        final_sentence = " ".join(sentence_list)
        return final_sentence