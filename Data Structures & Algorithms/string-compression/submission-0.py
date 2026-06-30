class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        count = 1
        write = 0
        for right in range(1,len(chars)):
            print(right)
            if chars[right] != chars[left]:
                
                chars[write] = chars[left]
                write +=1

                left = right
                if count >= 10:

                  
                    for ch in str(count):
                        chars[write] = ch
                        write +=1
                

                else:
                        if count > 1:
                            chars[write] = str(count)
                            write +=1
                   
                
                count = 1
            
            else:
                count+=1
                         
        chars[write] = chars[left]
        write +=1

        if count >= 10:

          for ch in str(count):
                chars[write] = ch
                write +=1
        else:
                if count > 1 :
                    chars[write] = str(count)
                    write +=1
                count = 1
        
        count = 1
        return write