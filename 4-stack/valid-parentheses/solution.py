class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                char_stack.append(c)
            else:
                if c == ")":
                    if len(char_stack) == 0 or char_stack[-1] != "(":
                        return False
                    else:
                        char_stack.pop()
                elif c == "]":
                    if len(char_stack) == 0 or char_stack[-1] != "[":
                        return False
                    else:
                        char_stack.pop()
                elif c == "}":
                    if len(char_stack) == 0 or char_stack[-1] != "{":
                        return False
                    else:
                        char_stack.pop()

        return len(char_stack) == 0


solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("[(({{(())}}))]"))
