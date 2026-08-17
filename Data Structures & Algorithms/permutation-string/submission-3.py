class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap1 , hashMap2 , left , right = {} , {} , 0 , len(s1)
        if len(s1) > len(s2):
            return False
        for char in s1:
            hashMap1[char] = hashMap1.get(char , 0) + 1

        for char in range(len(s1)):
            hashMap2[s2[char]] = hashMap2.get(s2[char] , 0) + 1

        if hashMap1 == hashMap2:
            return True

        while right < len(s2):

            hashMap2[s2[right]] = hashMap2.get(s2[right] , 0) + 1

            hashMap2[s2[left]] -=1

            if hashMap2[s2[left]] == 0:
                del hashMap2[s2[left]]

            if hashMap1 == hashMap2:
                return True
            
            left +=1
            right +=1

        return False
