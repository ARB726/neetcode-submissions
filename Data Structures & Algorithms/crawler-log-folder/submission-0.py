class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for st in logs:

            if st != "./" and st !="../":
                stack.append(st)

            elif stack and st!= "./" and st== "../":
                stack.pop()

                print(stack)
            
        return len(stack)