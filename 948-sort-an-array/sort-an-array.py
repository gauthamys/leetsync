class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            res = []
            la = 0
            lb = 0
            while la <= len(a) - 1 and lb <= len(b) - 1:
                if a[la] < b[lb]:
                    res.append(a[la])
                    la += 1
                else:
                    res.append(b[lb])
                    lb +=1
            if la == len(a):
                while lb < len(b):
                    res.append(b[lb])
                    lb += 1
            elif lb == len(b):
                while la < len(a):
                    res.append(a[la])
                    la += 1
            return res

        def sort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            leftSort = sort(left)
            rightSort = sort(right)
            return merge(leftSort, rightSort)
        
        return sort(nums)