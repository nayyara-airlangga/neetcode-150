class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        start_ptr, end_ptr = 0, 0
        length_of_longest = 0

        while end_ptr < len(s):
            while start_ptr < end_ptr and s[end_ptr] in s[start_ptr:end_ptr]:
                start_ptr += 1

            length_of_longest = max(length_of_longest, end_ptr - start_ptr + 1)

            end_ptr += 1

        return length_of_longest


solution = Solution()
print(solution.lengthOfLongestSubstring("pwwwkew"))
