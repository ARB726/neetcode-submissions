class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        newString = ""

        lenPreviousString = len(word1) + len(word2)

        while len(newString) != lenPreviousString:


            if left < len(word1) and right < len(word2):
                newString +=word1[left]
                newString +=word2[right]

                left +=1
                right +=1


                print(newString)
            elif left < len(word1) and right >= len(word2):
                newString +=word1[left]
                left +=1

            elif right < len(word2) and left >= len(word1):
                newString +=word2[right]
                right +=1


        return newString
