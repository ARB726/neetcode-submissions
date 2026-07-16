class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left , right , maxLength , hashMap = 0 , 0 ,0 , {}

        while right < len(s):

            hashMap[s[right]] = hashMap.get(s[right] , 0) + 1

            if (right-left+ 1) - max(hashMap.values()) > k:

                hashMap[s[left]] -=1
                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]
                left +=1


            # if len(hashMap) <= k:

            maxLength = max(maxLength , right - left + 1)

            right +=1

        
        return maxLength