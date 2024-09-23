class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # Base case: no extra character is needed for an empty substring

        # Convert the dictionary into set for O(1) lookup time
        word_set = set(dictionary)

        # Iterate through each position in the string
        for i in range(1, n + 1):
            # Skipping the current character
            dp[i] = dp[i - 1] + 1 # 1 extraa character

            # Check if any substring ending at position i matches with the word in dictionary
            for j in range(i):
                # If the substring from j to i is present in the string
                if s[j : i] in word_set:
                    # Update dp[i] with the minimum value between the current dp[i]
                    # and dp[j] (since no extra characters are needed for this substring)
                    dp[i] = min(dp[i], dp[j])

        return dp[n]

# if __name__ == "__main__":
#     # Read the input string 's'
#     s = input().strip() #.strip remove any leading or trailing spaces

#     # Read the size of dictionary
#     dict_size = int(input().strip())

#     # Read the words in the dictionary and store them in list
#     dictionary = []
#     for _ in range(dict_size):
#         dictionary.append(input().strip())

#     result = minExtraChar(s, dictionary)

#     print(result)


        
                    
