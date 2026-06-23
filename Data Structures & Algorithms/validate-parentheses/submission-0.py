class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={'(':')','{':'}','[':']'}
        for char in s:
            if char in map:
                stack.append(char)
            else:
                if not stack or map[stack[-1]]!=char:
                    return False
                stack.pop()
        return not stack