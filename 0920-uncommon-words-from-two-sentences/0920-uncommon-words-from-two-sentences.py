from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()

        count1 = Counter(words1)
        count2 = Counter(words2)

        combined_count = count1 + count2

        result = [word for word, count in combined_count.items() if count == 1]

        return result

    # TC: O(m + n) we are iterating through both the strings and processing each word once
    # SC: O(k) k: no of unique words

        # string1 = s1.split() # TC: O(m); m = len(s1)
        # string2 = s2.split() # TC: O(n); n = len(s2)
        # word_count = defaultdict(int) # Building the word dictionary TC: O(m + n)

        # for word1 in string1:
        #     word_count[word1] += 1
        
        # for word2 in string2:
        #     word_count[word2] += 1
        
        # result = [] # TC: O(m + n) in worst case

        # for word in word_count:
        #     if word_count[word] == 1:
        #         result.append(word)
        # return result

        # # TC: O(m + n)
        # # SC: O(m + n) for string1, string2, word_count and result respectively