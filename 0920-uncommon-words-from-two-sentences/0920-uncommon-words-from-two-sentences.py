class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        string1 = s1.split()
        string2 = s2.split()
        word_count = defaultdict(int)

        for word1 in string1:
            word_count[word1] += 1
        
        for word2 in string2:
            word_count[word2] += 1
        
        result = []

        for word in word_count:
            if word_count[word] == 1:
                result.append(word)
        return result