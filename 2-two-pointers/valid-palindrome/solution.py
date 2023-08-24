class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return True

        begin_ptr, end_ptr = 0, len(s) - 1

        while begin_ptr < end_ptr:
            while not s[begin_ptr].isalnum() and begin_ptr < len(s) - 1:
                begin_ptr += 1
            while not s[end_ptr].isalnum() and end_ptr > 0:
                end_ptr -= 1

            if not s[begin_ptr].isalnum() and not s[begin_ptr].isalnum():
                return True

            if s[begin_ptr].lower() != s[end_ptr].lower():
                return False

            begin_ptr += 1
            end_ptr -= 1

        return True


solution = Solution()
print(solution.isPalindrome("b.,a,ab."))
