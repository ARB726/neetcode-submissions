class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in see:
                return [see[compliment],i]
            see[nums[i]]=i
