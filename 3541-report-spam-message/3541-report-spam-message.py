class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        subset = set()
        count = 0
        for word in bannedWords:
            subset.add(word)

        for word in message:
            if word in subset:
                count += 1
                if count == 2:
                    return True
        return False