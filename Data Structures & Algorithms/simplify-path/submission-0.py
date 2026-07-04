class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for right in path.split("/"):
            print(right)

            if right == "." or right == "":
                pass
            
            elif stack and right == "..":
                stack.pop()

            elif not stack and right == "..":
                pass

            else:
                stack.append(right)

        return "/" + "/".join(stack)






