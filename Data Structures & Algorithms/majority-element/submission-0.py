class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)
        return max(count , key = count.get)