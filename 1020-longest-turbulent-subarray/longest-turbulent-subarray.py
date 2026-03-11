class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        
        ans = 1
        anchor = 0

        def compare(x, y):
            if x < y:
                return -1
            if x > y:
                return 1
            return 0
        
        for i in range(1, n):
            c = compare(arr[i - 1], arr[i])
            if c == 0:
                anchor = i
            else:
                if i == n - 1 or c * compare(arr[i], arr[i + 1]) != -1:
                    ans = max(ans, i - anchor + 1)
                    anchor = i
        
        return ans
            
