class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left , right , totalSums , minSize = 0 , 0 , 0 , float('inf')

        while right < len(nums):

            totalSums += nums[right]

            while totalSums >= target:

                totalSums -=nums[left]

                minSize = min(minSize , right - left +1)
                left +=1

            


            right +=1
        return 0 if isinstance(minSize , float) else minSize