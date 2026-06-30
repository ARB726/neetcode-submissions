class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        isEqual = False
        
        for right in asteroids:


            while stack and stack[-1] > 0 and right < 0:

                if stack[-1] == abs(right):
                    
                    stack.pop()
                    
                    isEqual = True
                    
                    break
                
                elif abs(stack[-1]) > abs(right):
                    isEqual = True
                    break
                else:

                    stack.pop()


            if not isEqual == True:

                stack.append(right)
            isEqual = False
        
        
        return stack