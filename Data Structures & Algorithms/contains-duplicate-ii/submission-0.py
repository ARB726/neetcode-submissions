class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set ()

        for i in range(len(nums)):

            if nums[i] in hashSet:
                return True

            hashSet.add(nums[i])

            if len(hashSet) > k:

                hashSet.remove(nums[i - k])

        return False