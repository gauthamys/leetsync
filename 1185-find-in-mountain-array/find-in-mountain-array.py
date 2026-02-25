# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n - 1
        
        # find peak
        while l < r:
            mid = (l + r) // 2
            midElem = mountainArr.get(mid)
            rightElem = mountainArr.get(mid + 1)
            
            if midElem > rightElem: # descending
                r = mid
            else:
                l = mid + 1
        
        peak = l

        if target > mountainArr.get(l):
            return -1
        
        def search(l, r, asc):
            while l <= r:
                mid = (l + r) // 2
                midElem = mountainArr.get(mid)
                if midElem == target:
                    return mid
                if asc:
                    if target > midElem:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if target < midElem:
                        l = mid + 1
                    else:
                        r = mid - 1
            return -1
        
        leftSearch = search(0, peak, True)
        if leftSearch != -1:
            return leftSearch
        
        return search(peak + 1, n - 1, False)

        