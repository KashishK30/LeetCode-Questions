class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, sub, point):
            count = 0
            stack = []
            for char in s:
                if stack and stack[-1] + char == sub:
                    stack.pop()
                    count += point
                else:
                    stack.append(char)
            return ''.join(stack), count               

        if x > y:
            s, points1 = remove_substring(s, "ab", x)
            _, points2 = remove_substring(s, "ba", y)
        if y > x:
            s, points1 = remove_substring(s, "ba", y)
            _, points2 = remove_substring(s, "ab", x)
        
        return points1 + points2