class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left , right , hashMap1 , hashMap2 , maxCount , result , have = 0 , 0 , {} , {} , float('inf') , "" , 0
        for char in t:
            hashMap1[char] = hashMap1.get(char , 0) + 1
        
        need = len(hashMap1)
      
        while right < len(s):

            hashMap2[s[right]] = hashMap2.get(s[right] , 0) + 1
            if s[right] in hashMap1 and hashMap2.get(s[right], 0) == hashMap1[s[right]]:
                have += 1
            while have == need:
                    if right - left + 1 < maxCount:
                        result = s[left:right+1]
                        maxCount = right - left + 1
                    
                    hashMap2[s[left]] = hashMap2.get(s[left] , 0) - 1
                    if s[left] in hashMap1 and hashMap2.get(s[left], 0) < hashMap1[s[left]]:
                        have -= 1
                    if hashMap2[s[left]] == 0:
                        
                        del hashMap2[s[left]]
                
                    left +=1

                
                    
            
            right +=1
        
        return result
        
        