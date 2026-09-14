class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = "".join(str(num) for num in digits)
        addResult = int(result) + 1
        return [int(char) for char in str(addResult)]