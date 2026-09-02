class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if (i > 0 and nums[i] == nums[i-1]): continue
            for j in range(i+1,n):
                if (j>i+1 and nums[j]==nums[j-1]): continue

                k = j + 1
                l = n-1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total > target:

                        l -=1

                    elif total < target:
                         k+=1

                    else:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        result.append(temp)
                        k+=1
                        l-=1

                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        # Skip duplicates for the fourth element
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                        
        return result











"""
NOTES:
1) Sort the list
2) create a two dimensional list
3) use a for loop to iterate if its the same number continue
4) use one more for loop to iterate if its the same number continue
5) create a variable to store j + 1
6) create a variable to store element n-1
"""
