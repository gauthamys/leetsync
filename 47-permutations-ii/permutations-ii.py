class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        path = []
        n = len(nums)

        def backtrack():
            if len(path) == n:
                res.append(path[:])
                return

            for x in count:
                if count[x] == 0:
                    continue
                count[x] -= 1
                path.append(x)
                backtrack()
                path.pop()
                count[x] += 1

        backtrack()
        return res