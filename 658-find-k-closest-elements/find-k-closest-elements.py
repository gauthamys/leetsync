class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = [(abs(arr[i] - x), i) for i in range(len(arr))]
        distances.sort(key=lambda x: x[0])

        return list(sorted([arr[x[1]] for x in distances][:k]))
