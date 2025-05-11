class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ans = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                ans = 0
            else:
                ans += 1
                if ans == 3:
                    return True
        return False
