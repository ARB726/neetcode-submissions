class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxCount , hashMap , left , right , result=float('-inf') , {} , 0 , 0 , []

        while right < len(nums):

            hashMap[nums[right]] = hashMap.get(nums[right] , 0) + 1

            while (right - left + 1) > k:

                hashMap[nums[left]] -=1

                if hashMap[nums[left]] == 0:
                    del hashMap[nums[left]]
                left +=1
            if (right-left+1) == k:   
                maxCount = max(hashMap.keys())
                result.append(maxCount)

            right +=1

        return result














