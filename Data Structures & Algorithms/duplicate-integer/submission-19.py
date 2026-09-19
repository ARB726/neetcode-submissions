class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm={}
        for num in range(len(nums)):
            hm[nums[num]]=hm.get(nums[num],0)+1
            if hm[nums[num]]>1:
                return True
        return False