class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Result  = [0]*len(temperatures)
        stack   = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                index = stack.pop()

                Result[index] = i - index

            stack.append(i)

        return Result