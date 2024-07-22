class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_num_str = sorted(num_str, reverse = True)

        if num_str == max_num_str:
            return num
        
        for i in range(len(num_str)):
            if num_str[i] != max_num_str[i]:
                for j in range(len(num_str) - 1, i, -1):
                    if num_str[j] == max_num_str[i]:
                        num_str[i], num_str[j] = num_str[j], num_str[i]
                        return int(''.join(num_str))
                        
        return int(''.join(num_str))

