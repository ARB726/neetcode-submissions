class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        Result = []
        for num in nums:
            Result.append(num)
            # print(Result)

        return Result
