class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hashmap = {0:1}
        remainingSum = 0

        for num in nums:
            remainingSum +=num

            if remainingSum-k in hashmap:
                count += hashmap[remainingSum - k]
            
            hashmap[remainingSum] = hashmap.get(remainingSum , 0 ) + 1

        return count