class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars_count = dict()
        for char in s:
            if char in s_chars_count:
                s_chars_count[char] += 1
            else:
                s_chars_count[char] = 1

        t_chars_count = dict()
        for char in t:
            if char in t_chars_count:
                t_chars_count[char] += 1
            else:
                t_chars_count[char] = 1

        for char in s_chars_count:
            if char not in t_chars_count:
                return False
            elif s_chars_count[char] != t_chars_count[char]:
                return False
            
        for char in t_chars_count:
            if char not in s_chars_count:
                return False
            elif s_chars_count[char] != t_chars_count[char]:
                return False

        return True