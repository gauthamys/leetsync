class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ar = [(abs(arr[i] - x), arr[i]) for i in range(len(arr))]
        ar.sort(key=lambda j: j[0])
        return list(sorted([i[1] for i in ar[:k]]))