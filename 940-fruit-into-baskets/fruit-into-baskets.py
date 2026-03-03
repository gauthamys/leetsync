class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # length of largest subarray with 2 distinct elements
        l, r = 0, 0
        m = {}
        res = float('-inf')
        while r < len(fruits):
            m[fruits[r]] = m.get(fruits[r], 0) + 1

            while l < len(fruits) and len(m) > 2:
                m[fruits[l]] -= 1
                if m[fruits[l]] == 0:
                    del m[fruits[l]]
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res
            