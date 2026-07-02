class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        freq = {'[':']' , '{':'}' , '(':')'}


        for right in s:

            if right in freq:
                stack.append(right)

            else:
                if stack and freq[stack[-1]] == right:
                    stack.pop()

                else:
                    return False

        if stack:
            return False
        else:
            return True