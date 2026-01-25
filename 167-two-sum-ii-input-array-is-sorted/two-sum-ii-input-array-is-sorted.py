class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                while numbers[l] == numbers[l + 1]:
                    l += 1
                l += 1
            elif s > target:
                r -= 1
        
        return [-1, -1]
             