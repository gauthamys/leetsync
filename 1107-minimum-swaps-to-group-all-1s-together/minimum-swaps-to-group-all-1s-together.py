class Solution:
    def minSwaps(self, data: List[int]) -> int:
        l, r = 0, 0
        ones = data.count(1)
        cnt_one = max_one = 0
        while r < len(data):
            cnt_one += 1 if data[r] == 1 else 0
            r += 1
            if r - l > ones:
                cnt_one -= 1 if data[l] == 1 else 0
                l += 1
            max_one = max(max_one, cnt_one)
        return ones - max_one
        
